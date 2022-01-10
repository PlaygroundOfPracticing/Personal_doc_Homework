import tensorflow as tf
import timeit
import numpy as np
import lstm_model
import pickle
import re
import pickle
import lstm_model
import pandas as pd

with open('model/chars.pkl', 'rb') as inp:
    chars = pickle.load(inp)
word_size = 128
maxlen = 96

model = lstm_model.create_model(maxlen, chars, word_size)
model.load_weights('model/model.h5', by_name=True)


zy = {'be': 0.75,
      'bm': 0.25,
      'eb': 0.5,
      'es': 0.5,
      'me': 0.75,
      'mm': 0.25,
      'sb': 0.5,
      'ss': 0.5
      }

zy = {i: np.log(zy[i]) for i in zy.keys()}


def viterbi(nodes):
    paths = {'b': nodes[0]['b'], 's': nodes[0]['s']}  # 第一层，只有两个节点
    for layer in range(1, len(nodes)):  # 后面的每一层
        paths_ = paths.copy()  # 先保存上一层的路径
        # node_now 为本层节点， node_last 为上层节点
        paths = {}  # 清空 path
        for node_now in nodes[layer].keys():
            # 对于本层的每个节点，找出最短路径
            sub_paths = {}
            # 上一层的每个节点到本层节点的连接
            for path_last in paths_.keys():
                if path_last[-1] + node_now in zy.keys():  # 若转移概率不为 0
                    sub_paths[path_last + node_now] = paths_[path_last] + nodes[layer][node_now] + zy[
                        path_last[-1] + node_now]
            # 最短路径,即概率最大的那个
            sr_subpaths = pd.Series(sub_paths)
            sr_subpaths = sr_subpaths.sort_values()  # 升序排序
            node_subpath = sr_subpaths.index[-1]  # 最短路径
            node_value = sr_subpaths[-1]  # 最短路径对应的值
            # 把 node_now 的最短路径添加到 paths 中
            paths[node_subpath] = node_value
    # 所有层求完后，找出最后一层中各个节点的路径最短的路径
    sr_paths = pd.Series(paths)
    sr_paths = sr_paths.sort_values()  # 按照升序排序
    return sr_paths.index[-1]  # 返回最短路径（概率值最大的路径）


def DirectPred(nodes):
    str = "";
    for node in nodes:
        predict = max(node, key=node.get)
        str += predict
    return str;


# nodes是为dict型
def simple_cut(s):
    if s:
        r = model.predict(np.array([list(chars[list(s)].fillna(0).astype(int)) + [0] * (maxlen - len(s))]),
                          verbose=False)[0][:len(s)]
        r = np.log(r)
        nodes = [dict(zip(['s', 'b', 'm', 'e'], i[:4])) for i in r]
        # t是序列，由两种方式取得。
        t = DirectPred(nodes)
        #t = viterbi(nodes)
        words = []
        for i in range(len(s)):
            if t[i] in ['s', 'b']:
                words.append(s[i])
            else:
                words[-1] += s[i]
        return words
    else:
        return []


not_cuts = re.compile(u'([\da-zA-Z ]+)|[。，、？！\.\?,!]')


def cut_word(s):
    result = []
    j = 0
    for i in not_cuts.finditer(s):
        result.extend(simple_cut(s[j:i.start()]))
        result.append(s[i.start():i.end()])
        j = i.end()
    result.extend(simple_cut(s[j:]))
    return result


with open('data/test2.txt', 'rb') as inp:
    texts = inp.read().decode('utf-8')
samples = texts.split('\r\n')

standards = []
with open('data/gold2.txt', 'rb') as labels:
    label = labels.read().decode('utf-8')
results = label.split('\r\n')
for result in results:
    standards.append(result.split())
    #print (result.split(), "*")

segmenteds = []
for sample in samples:
    #print(cut_word(sample), "**")
    segmenteds.append(cut_word(sample))


def statistics(standards, segmenteds): # 计算三值
    correctPred = 0
    wrongPred = 0
    totalLengthS = 0
    totalLengthSeg = 0
    i = 0
    for i in range(len(standards)):
        totalLengthS += len(standards[i]) # gold的分区数目
        totalLengthSeg += len(segmenteds[i]) # 分词结果的分区数目
        correctPred += len([x for x in standards[i] if x in segmenteds[i]])
        wrongPred += len([y for y in (standards[i] + segmenteds[i]) if y not in standards[i]])
    Precision = correctPred / totalLengthSeg
    Recall = correctPred / totalLengthS
    f1 = (2 * Precision * Recall) / (Precision + Recall)
    return Precision, Recall, f1

print(statistics(standards, segmenteds))