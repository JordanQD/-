'''
开发敏感词语过滤程序
设计一个函数，用来过滤输入字符串中的铭感字符串，如果遇到敏感字符串，则替换为5个星号字符“*****”。
提示1：函数的声明语句如下
def myfilter(source, speclist)
source表示待处理的字符串，敏感字符串用列表speclist存储。
提示2：可能用到字符串对象的查找函数find，替换函数replace。
'''

'''
def myfilter(source:str, speclist:list):
步骤:
tmpstr = source //直接在tmpstr内进行替换，最后返回tmpstr
for word in speclist:
   while True:
       在source中查找是否有word,得到索引 idx
       if idx >= 0 then
           tmpstr = source[0:iddx] + '*****' +source[idx+len(word):]
       else:
           break
       endif  
'''

def filter(source: str, speclist: list):
    tmpstr = source
    for word in speclist:
        while True:
            idx = tmpstr.find(word)
            if idx >= 0:
                tmpstr = tmpstr[0:idx] + '*****' + tmpstr[idx + len(word):]
            else:
                break
    return tmpstr

source = 'aabbccc_kkttkkuuccc'
wordlist = ['kk', 'ccc']
result = filter(source, wordlist)
print('result:', result)

#使用str.replace执行替换：
def filter(source: str, speclist: list):
    tmpstr = source
    for word in speclist:
        tmpstr = tmpstr.replace(word, '*****')
    return tmpstr

source = 'aabbccc_kkttkkuuccc'
wordlist = ['kk', 'ccc']
result = filter(source, wordlist)
print('result:', result)