import jieba
import joblib
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

import time
startTime = time.time()


def tfidf(sentence_data):
    tfidfVectorizer = TfidfVectorizer()
    sentence_data = [' '.join(jieba.cut(s, cut_all=False)) for s in sentence_data]
    word_to_vec = tfidfVectorizer.fit_transform(sentence_data)
    word_to_matrix = pd.DataFrame(word_to_vec.toarray())
    print(word_to_matrix.shape)
    return word_to_matrix


def predict_matrix(sentence, wordlist):
    feature_list = []
    sentence_to_word = jieba.lcut(sentence)
    for i in range(len(wordlist)):
        if wordlist[i] in set(sentence_to_word):
            feature_list.append(1)
        else:
            feature_list.append(0)
    return np.array(feature_list)


dataPath = './data/all.csv'
dataFrame = pd.read_csv(dataPath)
x_data = dataFrame['sentence']
y_data = dataFrame['label']
word_list = []
for x in x_data:
    word_list.extend(jieba.lcut(x))
word_list = list(set(word_list))

label_matrix = np.array(y_data)
x_train, x_test, y_train, y_test = train_test_split(tfidf(x_data), label_matrix,
                                                 test_size=0.2, random_state=42)#


def train_svm(sentence_data, label_data):
    # svc = svm.SVC(verbose=True)
    # parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 1.5, 2, 2.5, 10], 'gamma': [0.125, 0.25, 0.5, 1, 1.5, 2]}
    # clf = GridSearchCV(svc, parameters, scoring='f1')
    # clf.fit(sentence_data, label_data)
    # print('best parameter：')
    # print(clf.best_params_)
    clf = svm.SVC(kernel='rbf', C=10, gamma=0.5, verbose=True)
    clf.fit(sentence_data, label_data)
    print('model saving...')
    joblib.dump(clf, './model/svm.pkl')
    print('compelete!')
    return clf


clf = train_svm(x_train, y_train)
y_predict = clf.predict(x_test)
print('accuracy:', accuracy_score(y_predict, y_test))
print('f1-score', f1_score(y_predict, y_test))
# strSample = '今天天气虽然不错, 但是我很难受。'
# sample = predict_matrix(strSample, word_list[:-382])
# print(clf.predict([sample]))
print('运行时间：'+str(time.time()-startTime))
