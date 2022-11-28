'''
属性有 power,name，分别代表体力值和英雄的名子，体力值默认为 100;
方法有
1.) go() //行走的方法，如果体力值为 0，则输出不能行走，此英雄已死亡的信息
2.) eat(int n); //吃的方法，参数是补充的血量，将 n 的值加到属性 power 中，power 的值最 大为 100，
3.) hurt();//每受到一次伤害，体力值-10，体力值最小不能小于 0
'''

class Hero(object):
    def __init__(self, power, name):
        self.power = power
        self.name = name

    def go(self):
        if self.power == 0:
            print("No walking, die")
        else:
            print("Moving forward")
    
    def eat(self, int n):
        
