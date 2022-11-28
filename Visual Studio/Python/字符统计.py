'''
(1)输入一行字符(仅含英文字母)，编写函数分别统计各个字符的个数，不区分大小写.
(2)输入一行字符，编写函数统计出四类字母的数量: 英文字母、空格、数字和其它字符的个数。
分别编写一个函数，完成上述功能。

提示: 设d为一个dict对象,其"值"为"键"(字符)出现的次数.
1.返回一个字典对象: d[keyvalue]
2.如果当前字符为keyvalue,则 d[keyvalue] += 1 增加一次出现次数.
'''

#第一题
def count1(string):
    garge = {}
    for c in string:
        if c in garge:
            garge[c] += 1
        else:
            garge[c] = 1
    return garge

'''
s = input('输入：')
garge = count1(s.lower())
print(garge)
'''

#第2题
def count2(string):
    garge = {'Word': 0, 'Number': 0, 'Blank': 0, 'Other': 0}
    for c in string:
        if c.isalpha():
            garge['Word'] += 1
        elif c.isdigit():
            garge['Number'] += 1
        elif c.isspace():
            garge['Blank'] += 1
        else:
            garge['Other'] += 1
    return garge

s = input('输入：') #123123qweewerwe()  (_=)
print(count2(s))