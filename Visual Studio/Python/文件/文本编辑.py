'''
编辑一个文本文件: mytextfile.txt，保存到D盘（'D:\'）或C盘根目录('C:\')下.
包含下列4行文本:
first line
second line
third line
77 88 99
'''

'''
t='lloabcdehghellolol'.strip('lo') #
print(t)
t='lloabcdehghellolol'.lstrip('lo') #
print(t)
t='lloabcdehghellolol'.rstrip('lo') #
print(t)
# startwiths,endwiths
'''

filename = "/Users/jordan_qd/Desktop/mytextfile.txt"
fp = open(filename, 'rt')
L = []
L.append(fp.readline().strip())
fp.close()
print(L)


'''
filename = "C:/mytextfile.txt"
fp = open(filename,'rt')
L = []
L.append(fp.readline().strip())
L.append(fp.readline().strip())
L.append(fp.readline().strip())
L.append(fp.readline().strip())
fp.close()
print('file content:')
print(L)
'''