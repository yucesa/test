def fib(max):
    a = 0
    while a<max*10000:
        yield a
        a = (a+5)


f = fib(10)
for i in f:
    print(i)