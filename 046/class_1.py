class MyDecriptor():
    def __get__(self, instance, owner):
        print('getting',self,instance,owner)
    def __set__(self, instance, value):
        print('set',self,instance,value)
    def __delete__(self, instance):
        print('del',self,instance)

class Test():
    x=MyDecriptor()

test=Test()
print(test.x)
test.x='aaa'
del test.x

class MyProperty():
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        return self.fset(instance,value)
    def __delete__(self, instance):
        return self.fdel(instance)

class C:
    def __init__(self):
        self.x=None
    def getX(self):
        return self._x
    def setX(self,value):
        self._x=value
    def delX(self):
        del self._x
    x=MyProperty(getX,setX,delX)

c=C()
c.x='x-man'
c.x
