'''
def myGen():
    print('生成器被执行')
    yield 1
    yield 2


for i in myGen():
    print(i)
'''
def libs():
    a=0
    b=1
    while True:
        a,b=b,a+b
        yield a #注意缩进


for each in libs():
    if each >100:
        break
    print(each,end=' ')