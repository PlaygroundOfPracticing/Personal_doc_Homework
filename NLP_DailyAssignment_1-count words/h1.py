str_ = "The issue of employment has always been the concerning focus of the wholl society. The time is going on and people's view on job-hopping are changing too. Some people like engaging in one kind of job consistently. In Easten World, such as China, Japan, most people hold this opinion. It is partly influenced by the national culture. These people aren't pleasant to change. All they want or persuit is a stable and peace life. So they do a job only to earn money to leave on, even they don't interested in what they're doing. To them, that's enough. Whether these people like their job or not, they are sure to try their best to do everything well. We can often see that people always serve one company in loyalty through their lives. Unlike the people above-mentioned  some persons change their job constently  For instance, most Americans are the typical examples. They hate?stationery\". They more persuit stimulativity  Besides they hope their job to be chanllegable  so that they can show their capacity adequately. In their views, changing is reasonable. In my opionion  people have free right to chose a job. Nowadays, people should change with the world. In keen competitive society, people should think more about survival. So I think, the correct attitude to chose job is that: everyone must select one position that he or she is interested in and compatable to. In the position, you're confident that you can do it much better than any other. Of course, you should be qualified for it first. So whether you change your job or not, is not important. The critical thing is that you can do your work well and you're sure that it is the just work you need."

l_str = str_.strip().split()
str_dict = dict()
for s in l_str:
    if s in str_dict.keys():
        str_dict[s] += 1
    else:
        str_dict[s] = 1

# print(str_dict)

m_dict = sorted(str_dict.items(), key=lambda x: x[0], reverse=False)
# print(m_dict)
print("名字排序：")
for i in m_dict[:20]:
    print(str(i[0])+" : ", i[1]/len(l_str))

p_dict = sorted(str_dict.items(), key=lambda x: x[1], reverse=True)
# print(p_dict)
print("频率排序（降序）：")
for i in p_dict[:20]:
    print(str(i[0])+" : ", i[1]/len(l_str))

print("文章总词语数量：", len(l_str))
