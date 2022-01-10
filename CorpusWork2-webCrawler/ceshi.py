import re
import urllib
import urllib.request as request
url = 'https://news.gdufs.edu.cn/xyxw/1188.htm'
sitePrefix = 'https://news.gdufs.edu.cn/'
text = request.urlopen(url)
result = text.read().decode('utf-8')

# 获取网页标题
patternT = re.compile(r'<a href=".*info/.*" target="_blank" title=".*">(.*)</a>')
title = re.findall(patternT, result)
print(title[14:])

# 获取标题连接
patternL = re.compile(r'info/\d*/\d*.htm')
articleLink = re.findall(patternL, result)
articleLink = articleLink[22::3]
for i in range(12):
    articleLink[i] = sitePrefix + articleLink[i]

# 获取文章内容，循环读articleLink。
patternDel = re.compile(r'\r|\t|\n')    # 去除控制符
patternA = re.compile(r'<p class="vsbcontent_start">.*</p>')
patternTime = re.compile(r'发布时间：.*-\d{2}')

# 写入当前页面所有文章。
# for i in range(12):
#     articleRaw = request.urlopen(articleLink[i])
#     articleRaw = articleRaw.read().decode('utf-8')
#     articleTime = re.findall(patternTime, articleRaw)
#     article = re.sub(patternDel, '', articleRaw)
#     article = re.findall(patternA, article)
#     # newsList = open('newsList.txt', 'a')
#     # newsList.write('<article title="' + title[i] + '">\n'
#     #                 '<time>' + articleTime[0] + '</time>\n'
#     #                 '<content>' + article[0] + '</content>\n'
#     #                 '</article>\n')
#     # newsList.close()