class Parent():
    def hello(self):
        print('正在调用父类的方法')

class Child(Parent):
    pass

p=Parent()
c=Child()
print(p.hello())
print(c.hello())
class Child(Parent):
    def hello(self):
        print('正在调用子类的方法')

c=Child()
c.hello()