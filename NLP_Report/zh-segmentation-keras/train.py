# -*- coding:utf-8 -*-

import re
import numpy as np
import pandas as pd
import lstm_model
import pickle
from keras.utils import np_utils
from keras.backend.tensorflow_backend import set_session
import os
import tensorflow as tf

# 指定显卡以及限定显存使用率
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

# 设计模型
word_size = 128
maxlen = 32

with open('A:/pStudy/GithubRepository/NLP_finalwork/zh-segmentation-keras/data/msr_train.txt', 'rb') as inp:
    texts = inp.read().decode('gbk')
s = texts.split('\r\n')  # 根据换行切分


def clean(s):  # 整理一下数据，有些不规范的地方
    if u'“/s' not in s:
        return s.replace(u' ”/s', '')
    elif u'”/s' not in s:
        return s.replace(u'“/s ', '')
    elif u'‘/s' not in s:
        return s.replace(u' ’/s', '')
    elif u'’/s' not in s:
        return s.replace(u'‘/s ', '')
    else:
        return s


s = u''.join(map(clean, s))
s = re.split(u'[，。！？、]/[bems]', s)

data = []  # 生成训练样本
label = []


def get_xy(s):
    s = re.findall('(.)/(.)', s)
    if s:
        s = np.array(s)
        return list(s[:, 0]), list(s[:, 1])


for i in s:
    x = get_xy(i)
    if x:
        data.append(x[0])
        label.append(x[1])

d = pd.DataFrame(index=range(len(data)))
d['data'] = data
d['label'] = label
d = d[d['data'].apply(len) <= maxlen]
d.index = range(len(d))
tag = pd.Series({'s': 0, 'b': 1, 'm': 2, 'e': 3, 'x': 4})

chars = []  # 统计所有字，跟每个字编号
for i in data:
    chars.extend(i)
chars = pd.Series(chars).value_counts()
chars[:] = range(1, len(chars) + 1)

# 保存数据
with open('model/chars.pkl', 'wb') as outp:
    pickle.dump(chars, outp)
print('训练数据载入完毕')

# 生成适合模型输入的格式
d['x'] = d['data'].apply(lambda x: np.array(list(chars[x]) + [0] * (maxlen - len(x))))


def trans_one(x):
    _ = map(lambda y: np_utils.to_categorical(y, 5), tag[x].values.reshape((-1, 1)))
    _ = list(_)
    _.extend([np.array([[0, 0, 0, 0, 1]])] * (maxlen - len(x)))
    return np.array(_)


d['y'] = d['label'].apply(trans_one)

def train_bilstm():

    print("开始训练BiLSTM")
    model = lstm_model.create_model(maxlen, chars, word_size)
    batch_size = 128
    history = model.fit(np.array(list(d['x'])), np.array(list(d['y'])).reshape((-1, maxlen, 5)), batch_size=batch_size,
                        epochs=20, verbose=2)
    model.save('model/model.h5')

train_bilstm()
