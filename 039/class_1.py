'''
class Ball:
    def setName(self,name):
        self.name = name
    def kick(self):
        print('%s shuitiwo' % self.name)

a=Ball()
a.setName('A')
b=Ball()
b.setName('B')
c=Ball()
c.setName('C')

a.kick()
c.kick()
'''
'''
class Ball:
    def __init__(self,name):
        self.name=name
    def kick(self):
        print('%s shuitiwo' % self.name)

b= Ball('tudou')
b.kick()
'''
'''
class Person:
    name= 'a'

P=Person()
P.name
'''
class Person:
    __name= 'a'
    def getName(self):
        return self.__name

P=Person()
print(P._Person__name)