'''
f = open('C:\\Users\\Mr.Nan\\Desktop\\record.txt',encoding='UTF8')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy' + str(count) + '.txt'
        file_name_girl = 'girl' + str(count) + '.txt'

        boy_file = open(file_name_boy,'w',encoding='UTF8')
        girl_file = open(file_name_girl,'w',encoding='UTF8')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()
        boy = []
        girl = []
        count +=1

file_name_boy = 'boy' + str(count) + '.txt'
file_name_girl = 'girl' + str(count) + '.txt'

boy_file = open(file_name_boy,'w',encoding='UTF8')
girl_file = open(file_name_girl,'w',encoding='UTF8')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()
f.close()
'''
'''
f = open('C:\\Users\\Mr.Nan\\Desktop\\record.txt',encoding='UTF8')
def save_file(boy,girl,count):
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w', encoding='UTF8')
    girl_file = open(file_name_girl, 'w', encoding='UTF8')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        save_file(boy,girl,count)
        count +=1
        
save_file(boy,girl,count)
f.close()
'''
def save_file(boy,girl,count):
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w', encoding='UTF8')
    girl_file = open(file_name_girl, 'w', encoding='UTF8')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    f = open(file_name, encoding='UTF8')
    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)
            count += 1

    save_file(boy, girl, count)
    f.close()

split_file('f:/python/Study_python/029/record.txt')