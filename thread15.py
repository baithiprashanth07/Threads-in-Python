from threading import *
from time import *
def display():
    for i in range(5):
        print('Normal thread:', end='')
        print(i+1)
        sleep(1)
def display_time():
    while True:
        print('Damemon thread:',end='')
        print(ctime())
        sleep(2)

t=Thread(target=display)
t.start()
d=Thread(target=display_time)
d.daemon=True
d.start()
