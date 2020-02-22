#about dict.*()
dict1=dict.fromkeys(range(32),'赞')
for eachkeys in dict1.keys():
    print(eachkeys)

for eachValues in dict1.values():
    print(eachkeys)

for eachItems in dict1.items():
    print(eachItems)


print(dict1.get(32))
print(dict1.get(32,'没有'))
print(dict1.get(31,'没有'))

print(31 in dict1)

print(31 not in dict1)

dict1.clear()
print(dict1)
