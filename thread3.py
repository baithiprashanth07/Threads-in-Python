from threading import Thread
class MyThread(Thread):
    def run(self):
        for i in range(1,6):
            print(i)
t1=MyThread()
t1.start()
t1.join()
