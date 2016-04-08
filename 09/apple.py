import time

def foo(bar):
    return bar

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

def wrapper(f):
    def inner(*arg):
        print f.func_name + str(arg)
        return f(*arg)
    return inner

def timer(f):
    def inner(*arg):
        t0 = time.time()
        f(*arg)
        t1 = time.time()
        return t1 - t0
    return inner

if __name__ == '__main__':
    fib = wrapper(fib)
    print fib(2)
    print
    print timer(foo)(234)
