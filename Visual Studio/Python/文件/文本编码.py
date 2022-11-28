a = '哈哈哈'    
#Unicode -> gb2312
u_gb2312 = a.encode('gb2312')  
print('哈哈哈的gb2312编码为：',u_gb2312)
#Unicode -> utf-8
g_utf8 = a.encode('utf-8')  
print('哈哈哈的utf-8编码为：',g_utf8)

a='哈喽Hello'
print(a)
b=a.encode('gb2312')
print(b)
#c=b.decode()
#print(c)
d=b.decode('gb2312')
print(d)