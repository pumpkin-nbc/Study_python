import random
sercet =random.randint(1,10)
print(sercet)
print('------------------------')
temp=int(input("please write a number"))
guess=int(temp)
while guess !=sercet:
    temp=input("please write a number")
    guess=int(temp)
    if guess == sercet:
        print("you are right")
    else:
        if guess > sercet:
            print("it's big")
        else:
            print("it's small")
print("stop")
