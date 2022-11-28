class Box(object):
    def __init__(self, length, weigth, height):
        self.lenght = length
        self.weight = weigth
        self.height = height
    def volumn(self):
        return (self.length * self.weight * self.height)
    def superficial(self):
        return (2 * (self.length * self.weight + self.lenght * self.height + self.weight * self.height))

box1 = Box(1,2,3)
print(box1.volumn(), box1.superficial())