from threading import *
class MyThread(Thread):
    def __init__(self,str):
        Thread.__init__(self)
        self.str=str
    def run(self):
        print(self.str)
t1=MyThread('Hello')
t1.start()
t1.join()
