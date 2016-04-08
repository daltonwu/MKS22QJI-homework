import time

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

@wrapper
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

@timer
def foo(bar):
    return (bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar * bar *
bar)

if __name__ == '__main__':
    print fib(2)
    print
    print foo(234)
