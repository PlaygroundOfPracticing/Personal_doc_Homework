class seg(object):
    def __init__(self, inputstr, maxlen):
        self.segstring = inputstr
        self.MaxLen = maxlen
        self.Len = self.MaxLen
        self.indexpos = 0
        self.result = ""
        self.Bresult = ""
        self.Dict = {}

    def ReadDic(self):
        with open('./chineseDic.txt', "r") as f:  # 设置文件对象
            str_ = f.readlines()
        for i in str_:
            l = i.split(",")      #"石柱",n,  words=["石柱","n"]
            word = l[0]
            cx = l[1]
            self.Dict[word] = cx

    def MM_Seg(self):
    # 正向最大匹配算法
        seg.ReadDic(self)   # 读入字典
        seg.MM(self, self.segstring, self.MaxLen, 0)#正向最大分词
        seg.RMM(self, self.segstring, self.MaxLen, len(self.segstring)-1)#反向最大分词
        R = [self.result, self.Bresult]
        return R

    def MM(self, sentence, Len, indexpos):
        str = sentence
        l = Len
        frompos = indexpos

        if frompos + 1 == len(str):     # 该种情况是frompos指向最后一个字
            self.result = self.result + str[len(str)-1] + "/ "
            return
        # if frompos + 1 > len(str):
        #     return

        curstr=""
        llen = len(str)-(frompos+1)  # 剩余字符串长度
        if(llen < l):                          # //修改了
            curstr = str[frompos:frompos+llen+1]  # //修改了   把最后的 长度不够len的字符串 当成要切分的字符串

        else:
            curstr=str[frompos:frompos+l]

        if curstr in self.Dict.keys():
            self.result = self.result+curstr+"/ "
            L = self.MaxLen
            indexpos = frompos+l
            seg.MM(self,str,L,indexpos)

        else:
            if l > 1:

                l = l-1
                seg.MM(self,str,l,frompos)

            else:
                self.result = self.result+str[frompos:frompos+l]+"/ "     #//原：result=result+str+"/ "; ——当有单字时，加整个字符串str？？错误，
                                                                #  // 之所以没出错是因为前面83中，大部分单字存在于词典中
                frompos = frompos+1
                L = self.MaxLen
                seg.MM(self, str, L, frompos)

    def RMM(self,str,l,frompos):

        if(frompos == 0):     #//该种情况是frompos指向第一个字
            self.Bresult= str[0:1]+"/ "+self.Bresult
            return
        if frompos-1 < 0:
            return

        curstr=""
        llen=frompos+1  #//剩余字符串长度
        if(llen<l):                                    #//修改了
           curstr=str[0:frompos+1]  #//修改了   把最后的 长度不够len的字符串 当成要切分的字符串

        else:
            curstr=str[frompos-l+1:frompos+1]

        if curstr in self.Dict.keys():
            self.Bresult= curstr+ "/ "+self.Bresult
            L=self.MaxLen
            indexpos=frompos-l
            seg.RMM(self,str,L,indexpos)

        else:
            if l>1:
                L=l-1
                seg.RMM(self,str,L,frompos)
            else:
                self.Bresult= str.substring(frompos ,frompos+1)+"/ " + self.Bresult     #//原：result=result+str+"/ "; ——当有单字时，加整个字符串str？？错误，
                #// 之所以没出错是因为前面83中，大部分单字存在于词典中
                frompos=frompos - 1
                l=self.MaxLen
                seg.RMM(self,str,l,frompos)

    def GetResult(self):
        return self.result

    def getBresult(self):
        return self.Bresult

def main():
    # a = seg("在这一年中，中国的改革开放和现代化建设继续向前迈进。国民经济保持了“高增长、低通胀”的良好发展态势。农业生产再次获得好的收成，企业改革继续深化，人民生活进一步改善。对外经济技术合作与交流不断扩大。",3);
    a = seg("去年今日此门中，人面桃花相映红。", 4)
    a.MM_Seg()
    print(a.GetResult())
    # print(a.getBresult())
    print(a.result)
    # print(a.Bresult)

if __name__ == '__main__':
    main()

# //    public static void main(String[] args) throws IOException, Exception
# //    {
# //
# //        seg s=new seg("在这一年中，中国的改革开放和现代化建设继续向前迈进。国民经济保持了“高增长、低通胀”的良好发展态势。农业生产再次获得好的收成，企业改革继续深化，人民生活进一步改善。对外经济技术合作与交流不断扩大。",3);
# //
# //        String [] Bresult =s.MM_Seg();
# //
# //
# //        System.out.println("正向：");
# //        System.out.println(Bresult[0]);
# //        System.out.println("反向：");
# //        System.out.println(Bresult[1]);
# //
# //
# //    }
#
#
