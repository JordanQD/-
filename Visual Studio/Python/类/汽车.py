#定义一个汽车类(Car)，属性有颜色，品牌，车牌号，价格，并实例化两个对象，给属性赋值，并输入属性值。
class car(object):
    def __init__(self, color, board, number, price):
        self.color = color
        self.board = board
        self.number = number
        self.price = price
    def driver(self):
        print(self.color, self.board, self.number, self.price)

car1 = car('blue', 'benz', 'ZASB250', 123456)
car1.board = 'volkswagon'
car1.driver()
