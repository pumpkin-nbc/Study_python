'''
class C:
    def __init__(self):
        self.x='x-man'


c=C()
c.x
getattr(c,'x','没有这个属性')

class C:
    def __init__(self):
        self.size=size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)
'''
'''
#__getattribute__定义
class C():
    def __getattribute__(self, name):
        print('__getattribute__') #定义当该类的属性被访问时的行为
        return super().__getattribute__(name)
    def __getattr__(self, name):
        print('getattr')  #定义当用户试图获取一个不存在的属性时的行为
    def __setattr__(self, name, value):
        print('setattr') #定义当一个属性被设置时的行为
        super().__setattr__(name,value)
    def __delattr__(self, name):
        print('delattr') #定义当一个属性被删除的行为
        super().__delattr__(name)
'''
class Rectangle():
    def __init__(self,width=0,height=0):
        self.height=height
        self.width=width

    def __setattr__(self, name, value):
        if name =='square':
            self.width=value
            self.height=value
        else:
            super().__setattr__(name,value)
            #self.__dict__[name]=value

    def getArea(self):
        return self.width * self.height
