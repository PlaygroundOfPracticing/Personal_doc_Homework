import time
import jieba
import re
start_time = time.time()

with open("text.txt", "r", encoding='utf-8') as f:
    text = f.read()

# 去除词性标注、空格以及年份标记，result是为处理之后的str。
pattern = re.compile(r'/[a-zA-Z]+\s\s')
result = re.sub(pattern, '', text)
pattern = re.compile(r'(\d*)-(\d*)-(\d*)-(\d*)')
result = re.sub(pattern, '', result)

dict = {}
for i in result:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

# 统计字数，统计非重复字数（输出键的个数：4708）
# print(dict)
# print(len(dict))

# 使用jieba包进行中文分词，同样用词典进行统计
result = jieba.lcut(result)
wordDict = {}
for i in result:
    if i not in wordDict:
        wordDict[i] = 1
    else:
        wordDict[i] += 1

# 统计词数，统计非重复词数
# print(wordDict)
# print(len(wordDict))

# 统计词频
count = {}
for word in wordDict:
    # 将标点符号，单字作为停用词
    if len(word) == 1:
        continue
    count[word] = wordDict[word]

# 经典的根据字典键/值排序的写法。
top50 = sorted(count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
bottom50 = sorted(count.items(), key=lambda kv: (kv[1], kv[0]), reverse=False)
for i in range(50):
    print(top50[i], bottom50[i])

# 计算换行符个数
with open("text.txt", "r", encoding='utf-8') as f:
    text = f.readlines()
blank_num = 0

for line in text:
    line = line.strip()
    if line == '':
        blank_num = blank_num+1
print(blank_num)

end_time = time.time()
print("运行总时长：", end_time - start_time)
