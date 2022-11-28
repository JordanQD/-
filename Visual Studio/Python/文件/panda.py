import struct

filename = 'mytest.dat'
fobj = open(filename,'wb')

a = [100,200,300,1000,2000,3000]
fmt = 'llllll'
d = struct.pack(fmt,a[0],a[1],a[2],a[3],a[4],a[5])
fobj.write(d)
b = a.copy()
for i in range(len(a)):
    b[i] *= 2
d = struct.pack(fmt,b[0],b[1],b[2],b[3],b[4],b[5])
fobj.write(d)
fobj.close()

#filename = 'mytest.dat'
fobj = open(filename,'rb')
#fmt = 'llllll'
d = fobj.read(24)
v1 = struct.unpack(fmt,d)
print('前6个整数:',v1)

d = fobj.read(24)
v2 = struct.unpack(fmt,d)
print('后6个整数:',v2)

fobj.close()