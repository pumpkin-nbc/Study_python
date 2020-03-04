import easygui as g
import sys

while 1:
     g.msgbox('小游戏')

     msg='请问'
     title='小游戏互动'
     choices=['1','2','3']

     choice=g.choicebox(msg,title,choices)

     g.msgbox('你的选择是'+ str(choice),'结果')
     msg = '重新开始'
     title='请选择'

     if g.ccbox(msg,title):
         pass
     else:
         sys.exit(0)