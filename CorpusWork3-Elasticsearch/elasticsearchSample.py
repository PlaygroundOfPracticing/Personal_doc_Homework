from elasticsearch import Elasticsearch
import json
import data
es = Elasticsearch(
    [
        {"host": "localhost", "port": "9200"}
    ]
)

mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}

datas = [
    {
        'title': '3080显卡评测',
        'url': 'https://www.expreview.com/76519.html',
        'date': '2020.11.16'
    },
    {
        'title': 'Intel正式发布第三代至强可扩展处理器，单芯最多可达40核。',
        'url': 'https://www.expreview.com/78594.html',
        'date': '2021.04.07'
    },
    {
        'title': '显示驱动芯片短缺导致生产延迟，业界人士称目前情况过去20年里前所未见。',
        'url': 'https://www.expreview.com/78593.html',
        'date': '2021.04.07'
    },
    {
        'title': '微软将服务器直接浸入液体进行散热，可能会成为未来数据中心常态。',
        'url': 'https://www.expreview.com/78592.html',
        'date': '2021.04.07'
    },
    {
        'title': '技嘉将推出X570S主板，可能是未AMD新处理器做准备。',
        'url': 'https://www.expreview.com/78590.html',
        'date': '2021.04.07'
    },
    {
        'title': 'E3 2021将于6月12日至15日以线上形式举办，索尼或继续缺席。',
        'url': 'https://www.expreview.com/78588.html',
        'date': '2021.04.07'
    },
    ]

dataMaths = [
    {
        'title': '高等数学',
        'url': 'https://www.expreview.com/76519.html',
        'date': '2020.11.16'
    },
    {
        'title': '高等数学之可微，可导，可积与连续之间的关系。',
        'url': 'https://blog.csdn.net/huxiaokang1234/article/details/52550999',
        'date': '2016.09.15'
    },
    {
        'title': '一元函数连续要点',
        'url': 'https://zhuanlan.zhihu.com/p/93400055',
        'date': '2019.12.02'
    },
    {
        'title': '一元函数可导可微连续的关系_一图学会函数连续、可导、可微的关系',
        'url': 'https://blog.csdn.net/weixin_39805644/article/details/113708398',
        'date': '2021.02.06'
    },
    {
        'title': '多元函数中的偏导数全导数以及隐函数',
        'url': 'https://blog.csdn.net/weixin_43314579/article/details/88937475',
        'date': '2019.03.31'

    },
    {
        'title': '【高等数学】多元复合函数求导的基本方法',
        'url': 'https://zhuanlan.zhihu.com/p/61585348',
        'date': '2020。03.18'
    },
]

# 以下代码需要运行一次，之后注释。
# # es.indices.delete(index='news', ignore=[400])
# es.indices.create(index='news', ignore=400)
#
# # es.indices.delete(index='math', ignore=[402])
# es.indices.create(index='math', ignore=402)

# result = es.indices.put_mapping(index='news', doc_type='science', body=mapping)
# result = es.indices.put_mapping(index='math', doc_type='course', body=mapping)

# for data in datas:
#     es.index(index='news', doc_type='science', body=data)
# for dataMath in dataMaths:
#     es.index(index='math', doc_type='course', body=dataMath)
# result = es.search(index='math', doc_type='course')

searchKeyWord = input()
dsl = {
    'query': {
        'match': {
            'title': searchKeyWord
        }
    }
}
result = es.search(index='math', body=dsl)
print(json.dumps(result, indent=2, ensure_ascii=False))
