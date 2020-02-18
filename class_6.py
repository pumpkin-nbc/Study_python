def fun1():
    x=5
    def fun2():
        nonlocal x
        x*=x
        return x
    return fun2()

print(fun1())