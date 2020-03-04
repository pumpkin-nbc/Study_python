class MyList(list):
    pass
List2=MyList()
List2.append(7)
print(List2)

class A:
    def fun(self):
        print('a')

class B:
    def fun(self):
        print('b')

a=A()
b=B()

a.fun()
b.fun()