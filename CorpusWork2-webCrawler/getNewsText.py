import re
import time
from bs4 import BeautifulSoup
import urllib
import urllib3
import urllib.request as request
import xml.sax
start_time = time.time()

patternT = re.compile(r'<a href=".*info/.*" target="_blank" title=".*">(.*)</a>')   # 获得标题
patternDel = re.compile(r'\r|\t|\n')  # 去除控制符
patternA = re.compile(r'<p class="vsbcontent_start">.*</p>')    # 获得正文
patternTime = re.compile(r'发布时间：.*-\d{2}')  # 时间
patternL = re.compile(r'info/\d*/\d*.htm')  # 新闻列表页下文章页连接
sitePrefix = 'https://news.gdufs.edu.cn/'

# 约500份文章，每个页面有12份，共需要500/12≈42页。
newsList = open('newsList.txt', 'a', encoding='utf-8')
for i in range(42):
    url = 'https://news.gdufs.edu.cn/xyxw/' + str(1188-i) + '.htm'
    text = request.urlopen(url)
    result = text.read().decode('utf-8')

    # 获取网页标题
    title = re.findall(patternT, result)
    # print(title[14:][8])

    # 获取标题对应的连接
    articleLink = re.findall(patternL, result)
    articleLink = articleLink[22::3]
    for j in range(12):
        articleLink[j] = sitePrefix + articleLink[j]

    # 获取文章内容，循环读articleLink。
    # 写入当前页面所有文章。
    for j in range(12):
        articleRaw = request.urlopen(articleLink[j])
        articleRaw = articleRaw.read().decode('utf-8')
        articleTime = re.findall(patternTime, articleRaw)
        article = re.sub(patternDel, '', articleRaw)
        article = re.findall(patternA, article)

        newsList.write('<article title="' + title[14:][j] + '">\n'
                        '<time>' + articleTime[0] + '</time>\n'
                        '<content>' + ''.join(article) + '</content>\n'
                        '</article>\n')
newsList.close()

end_time = time.time()
print("运行总时长：", end_time - start_time)