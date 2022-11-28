'''
一个人赶着鸭子去每个村庄卖，每经过一个村子卖去所赶鸭子的一半又一只。这样他经过了七个村子后还剩两只鸭子，问他出发时共赶多少只鸭子？经过每个村子卖出多少只鸭子?
'''

def count(ini, flag):
    '''
    flag -= 1
    ini = (ini + 1) * 2
    '''
    
    if flag == 0:
        return ini
    #print(count(ini, flag))
    
    return count((ini + 1) * 2, flag - 1)    #为啥加个return？

print(count(2,7))