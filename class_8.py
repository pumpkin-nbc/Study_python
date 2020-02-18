'''
#非递归版本
x=int(input('number'))
i=0
y=1
for i in range(x):
    y=x*y
    i+=1
    x-=1
    print(y)

print('zuihou:',y)

def factorial(n):
    result=n
    for i in range(1,n):
        result*=i
    return result

print(factorial(5))
'''
#递归版本
def factorial1(n):
    if n == 1:
        return 1
    else:
        return n * factorial1(n-1)

number=int(input('number'))
result1 = factorial1(number)
print(result1)