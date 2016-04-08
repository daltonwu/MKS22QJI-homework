def foo(bar):
    return bar

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

@fib
def wrapper(f):
    def inner(*arg):
        print f.func_name + str(arg)
        return f(*arg)
    return inner

if __name__ == '__main__':
    a = wrapper(fib)
    for n in range(10):
        print a(n)
