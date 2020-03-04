'''
class A():
    def __str__(self):
        return 'aaa'

class B():
    def __repr__(self):
        return 'bbbb'
'''
import time as t
class MyTimer():
    def __str__(self):
        return self.prompt

    __repr__=__str__

    def __init__(self):
        self.unit=['年','月','天','小时','分钟','秒']
        self.prompt='未开始计时'
        self.laset=[]
        self.begin=0
        self.end=0

    def __add__(self, other):
        prompt='总共运行了'
        result=[]
        for index in range(6):
            result.append(self.laset[index] + other.laset[index])
            if result[index]:
                prompt +=(str(result[index] + self.unit[index]))
        return prompt

    #开始计时
    def start(self):
        self.begin=t.localtime()
        self.prompt = '请先调用stop停止计时'
        print('计时开始')
    #停止计时
    def stop(self):
        if not self.begin:
            print('请先调用start进行计时！')
        else:
            self.end=t.localtime()
            self._calc()
            print('计时停止')

    #内部方法，计算运行时间
    def _calc(self):
        self.laset=[]
        self.prompt='总共运行了'
        for index in range(6):
            self.laset.append(self.end[index] - self.begin[index])
            if self.laset[index]:
                self.prompt +=str(abs(self.laset[index])) + self.unit[index]
        #为下一轮计时初始化
        self.begin=0
        self.end=0