from functools import lru_cache

@lru_cache(maxsize=500)
def fib(n):
    if n < 0:
        raise IndexError(
            'Index was negative. '
            'No such thing as a negative index in a series.'
        )
    elif n in [0, 1]:
        # Base cases
        return n
    print("computing fib(%i)" % n)
    return fib(n - 1) + fib(n - 2)




# ok now, the suboptimal way
cache = {}
def fib1(n):
    if n in cache:
        return cache[n]

    if n < 0:
        raise IndexError(
            'Index was negative. '
            'No such thing as a negative index in a series.'
        )
    elif n == 1 or n==2:
        value = 1
    elif n > 2:
        value = fib1(n - 1) + fib1(n - 2)
    cache[n] = value
    return value

print(fib1(500))