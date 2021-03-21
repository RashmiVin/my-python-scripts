# Fibonacci numbers module

def fib1(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        i = 0
        #print(a, end='')
        while i < a:
            print('-', end='')
            i += 1
        print()
        a, b = b, a+b
    print()


num = 300
fib1(num)
fib(num)