import threading
print(' let us find the current thread')
print('Currently running thread:',threading.current_thread().getName())
if threading.current_thread()== threading.main_thread():
    print('the current thread is the main thread')
else:
    print(' the current thread is the main thread')
    
