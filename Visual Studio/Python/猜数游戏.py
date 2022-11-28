'''
练习:
完成一个猜数游戏:
系统随机产生一个1-9的整数，用户可以最多猜3次；猜中了加1分，猜的数偏小提示“小了”，猜的数偏大提示“大了”。
'''

import random
score = 0
ans = random.randint(1, 9)
print(ans)
for a in range(3):
    num = int(input("请猜一个1～9中的数字："))
    if num == ans:
        score += 1
        break
    elif num > ans:
        print("太大了！")
    else:
        print("太小了！")
