from threading import *
class MyThread:
    def __init__(self,str):
        self.str=str
    def display(self,x,y):
        print(self.str)
        print('the args are:',x,y)
obj=MyThread('hello')
t1=Thread(target=obj.display,args=(1,2))
t1.start()
