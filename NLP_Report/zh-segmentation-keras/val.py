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
maxlen = 32

model = lstm_model.create_model(maxlen, chars, word_size)
model.load_weights('model/model.h5', by_name=True)


def DirectPred(nodes):
    str = "";
    for node in nodes:
        predict = max(node, key=node.get)
        str += predict
    print(str)
    return str;


def simple_cut(s):
    if s:
        r = model.predict(np.array([list(chars[list(s)].fillna(0).astype(int)) + [0] * (maxlen - len(s))]),
                          verbose=False)[0][:len(s)]
        r = np.log(r)
        probabilityList = [dict(zip(['s', 'b', 'm', 'e'], i[:4])) for i in r]
        print (probabilityList)
        t = DirectPred(probabilityList)
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

sample = "他马上功夫很好，要向全班同学报告书上的内容。我从小学习电脑。" \
         "部分居民生活水平。结合成分子时。结婚的和尚未结婚的。使用户体验更好。研究生命科学。"

print(cut_word(sample))
