# 裝飾器本質是一個函數，把被裝飾的函數當成參數
import time

def timer(func):
    def inner(*args, **kwargs):  #args 會成為元祖,數字， Kwargs會成為字典,'b'=4,
        for d in args:
            print(d)
        start = time.time()
        func(*args, **kwargs)
        print(time.time()-start)
    return inner

@timer
def Test(a, b, c):
    for i in range(100000):
        print(123)

Test(1, 2,3)