from threading import *
from time import *
class MyThread:
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print('Boil milk and tea power for 5 mintutes...',end='')
        sleep(5)
        print('Done')
    def task2(self):
        print('add sugar and boil for 3 mintutes...',end= '')
        sleep(3)
        print('Done')
    def task3(self):
        print('filter it and serve...',end='')
        print('Done')
obj=MyThread()
t= Thread(target=obj.prepareTea)
t.start()
    
