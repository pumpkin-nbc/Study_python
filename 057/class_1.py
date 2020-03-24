#正则表达式
import re
print(re.search(r'FishC','I love FishC.com')) #搜索第一次出现的位置
print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.111.111'))
print(re.search(r'ab{3}c','abbbc'))#{3}表示该大括号前面的字符重复三次
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-4]','192'))
print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-4])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-4])','192.168.1.1'))