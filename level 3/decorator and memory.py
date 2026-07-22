import functools
def memorize(func):
    memory ={}
    functools.wraps(func)
    def inner(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]
    return inner
@memorize
def fibonacci(n):
    if n == 0 or n ==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(100))


































































































