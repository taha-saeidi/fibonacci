def fib_gen():
    f1 = 0
    yield f1
    f2 = 1
    yield f2
    while True:
        f3 = f1+f2
        yield f3
        f1 = f2
        f2 = f3
g = fib_gen()
for i in range(10):
    print(next(g),end=" | ")


# اینو هم یه برنامه نویس تازه کار و noob نوشته































































































