Dict = {}
with open('./chineseDic.txt', "r") as f:  # 设置文件对象
    str_ = f.readlines()
for i in str_:
    l = i.split(",")
    word = l[0]
    cx = l[1]
    Dict[word] = cx


def mm(str, index, len):
    result = ''
    maxLen = len
    if str[index:index+len] in Dict:
        result += str[index:index+len] + '/'
        mm(str, index+len, len)
    else:
        if len > 1:
            len = len - 1
            mm(str, index, len)
        else:
            result += str[index:index+1] + '/'
            len = maxLen
            index = index + 1
            mm(str, index, len)

    return result

print(mm('我爱北京天安门。', 0, 3))

