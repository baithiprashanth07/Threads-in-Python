from threading import *
def display(str):
    print(str)
for i in range(6):
    t=Thread(target=display,args=('\n Hello',))
    t.start()
    
