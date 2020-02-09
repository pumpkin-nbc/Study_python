grade=int(input("please write your grade"))
if grade >=90:
    print('your grade is A')
elif grade >= 80 and grade <90:
    print('your grade is B')
elif grade <80 and grade >=60:
    print('your grade is C')
elif grade <60 and grade >=0:
    print('your grade is D')
else:
    print('not right')