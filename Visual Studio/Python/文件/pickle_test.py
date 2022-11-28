'''
使用pickle序列号一个dict对象；dict的vlaue尽量比较丰富.包含dict对象；list对象。步骤：
1.构造一个dict对象D；
2.将D序列化到文件mydicttest.pkl
3.将文件mydicttest.pkl反序列化为一个对象Dnew；
4.输出D和Dnew，观察二者的差异。
5.再序列化到string对象后，再反序列化（也就是使用pickle的dumps和loads方法）
'''

'''
# 序列化、反序列化操作: 不序列化到文件的示例
import pickle as pkl
D = {'101':11,'201':22,'301':33}
s = pkl.dumps(D)
print('type(s)',type(s))
print(s)
Dnew = pkl.loads(s)
print('D')
print(D)
print('Dnew')
print(Dnew)
'''


import pickle as pkl
list1= [1,3,5,{'name': 'Lisi',9:{'color':'Red','height':120}},[77,88,99]]
tuple1 = (35,39,49,56)
s1  = set(['a','c','d','h'])
D = {'101':list1,'201':tuple1,'301':s1,'401': 'Hello World'}
filename = 'mydicttest.pkl'
f = open(filename,'wb')
pkl.dump(D,f)
pkl.dump(list1,f)
f.close()
# 反序列化
f2 = open(filename,'rb')
Dnew = pkl.load(f2)
listnew = pkl.load(f2)
f2.close()
print('source data:')
print('D:')
print(D)
print('list1:')
print(list1)
print('after unpickle data:')
print('Dnew:')
print(Dnew)
print('listnew:')
print(listnew)
