def classmethod(func):
    def inner(*args,**kwargs):
        func('类')
    return inner

def staticmethod(func):
    def inner(*args,**kwargs):
        func()
    return inner

@staticmethod
def wahaha():
    print('in 娃哈哈')

@classmethod
def qqxing(cls):
    print('in qqxing',cls)

wahaha()
qqxing()

