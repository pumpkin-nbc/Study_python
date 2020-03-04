#issubclass(class,classinfo) 若class是classinfo的子类，这返回True
'''
class A:
    pass

class B(A):
    pass

print(issubclass(A,B))

class C:
    pass
'''
#isinstance(object,classinfo) 检查实例对象是否属于该类
'''
b1=B()
isinstance(b1,B)
'''

#hasattr(object,'name')  对象中是否有属性名 返回True或者false
'''
class C:
    def __init__(self,x=0):
        self.x=x

c1=C()
hasattr(c1,'x')
'''

#getattr(object,'name',default)  判断对象中是否有属性名，并返回值  若属性值不存在，则返回default

#setattr(object,'name','value') 判断对象中是否有属性名，若没有该属性则创建该属性，value设置值

#delattr(object,'name')  删除对象中的属性值

#property(fget=None,fset=None,fdel=None,doc=None) 通过属性设置属性 fget获得属性 fset设置属性 fdel删除属性
class C:
    def __init__(self,size=10):
        self.size=size

    def getSize(self):
        return  self.size
    def setSize(self,value):
        self.size=value
    def delSize(self):
        del self.size
    x=property(getSize,setSize,delSize)

c1=C()
print(c1.getSize())
print(c1.x)
