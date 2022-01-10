import xml.dom.minidom
import re
import os
import csv

import time

startTime = time.time()
path = './篇章依存树库1-100/'
pattern = re.compile(r'\d+、')
pattern2 = re.compile(r'[。？！；]')

Contents = []
for root, dirs, files in os.walk(path):  # 读取所有xml文件的content，存入Contents中。
    for file in files:
        dom = xml.dom.minidom.parse(root + file)
        element = dom.documentElement
        paragraph = element.getElementsByTagName('pragraph')

        for i in range(len(paragraph)):
            contents = str(paragraph[i].getAttribute('content'))
            Contents.append(contents)


# 构造label列表
sentenceText = []
sentenceLabel = []
count = 0

for i in range(len(Contents)):
    sentenceTemp = Contents[i].split('，')

    for j in range(len(sentenceTemp)):
        if j == len(sentenceTemp)-1 or re.search(pattern, sentenceTemp[j+1]):
            sentenceLabel.append(1)
            sentenceText.append(re.sub(pattern, '', sentenceTemp[j]))
        else:
            sentenceLabel.append(0)
            sentenceText.append(re.sub(pattern, '', sentenceTemp[j]))

f_pos = open('./data/pos.csv', 'w', encoding='utf-8-sig', newline='')
f_neg = open('./data/neg.csv', 'w', encoding='utf-8-sig', newline='')
f_all = open('./data/all.csv', 'w', encoding='utf-8-sig', newline='')

writer_pos = csv.writer(f_pos)
writer_pos.writerow(['id', 'sentence', 'label'])

writer_neg = csv.writer(f_neg)
writer_neg.writerow(['id', 'sentence', 'label'])

writer_all = csv.writer(f_all)
writer_all.writerow(['id', 'sentence', 'label'])

for i in range(len(sentenceLabel)):
    count += 1
    if sentenceLabel[i] == 1:
        writer_pos.writerow([count, sentenceText[i], 1])
    else:
        writer_neg.writerow([count, sentenceText[i], 0])

    writer_all.writerow([count, sentenceText[i], sentenceLabel[i]])

print('运行时间：'+str(time.time()-startTime))
