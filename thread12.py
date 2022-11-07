from threading import *
from time import *
class Producer:
    def __init__(self):
        self.lst=[]
        self.dataprodover=False
    def produce(self):
        for i in range(1,11):
            self.lst.append(i)
            sleep(1)
            print('Item produced..')
        self.datprodover=True
class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        while self.prod.dataprodover==False:
            sleep(0.1)
        print(self.prod.lst)
p=Producer()
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()
