try:
    f=open('111.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦'+str(reason))