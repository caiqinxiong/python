import os
import time
from multiprocessing import Process
def func1():
    print(123,os.getpid())
    time.sleep(1)
    print(456)

def func2():
    print('aaa',os.getpid())
    time.sleep(1)
    print('bbb')
if __name__ == '__main__':
    Process(target=func1).start()
    Process(target=func2).start()

# func1()
# func2()

