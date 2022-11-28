L_Source = [1, 5, 10, 20, 50, 100]
L_Total = [0, 0, 0, 0, 0, 0]

def myfun(K, L_Source, L_Total, L):
    for i in range(6):
        while K - L_Source[5-i] >= 0:
            if L[5-i] > 0:
                L[5-i] -= 1
                L_Total[5-i] += 1
                K = K - L_Source[5-i]
            else:
                i += 1
                
    for j in range(6):
        print(L_Source[j], ':', L_Total[j])

K, c0, c1, c2, c3, c4, c5 = map(int, input('输入K和各种零钱的数量（从小到大）用空格隔开:').split())
L = [c0, c1, c2, c3, c4, c5]

myfun(K, L_Source, L_Total, L)
