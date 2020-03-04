class Turtle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def print_num(self):
        print('乌龟、鱼数量',self.turtle.num,self.fish.num)

pool=Pool(1,2)
pool.print_num()