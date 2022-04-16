from functools import lru_cache


@lru_cache(maxsize=1000)
def f(n):
    if n == 1:
        return 1
    elif n >= 2:
        return f(n-1) - 2*g(n-1)


@lru_cache(maxsize=1000)
def g(n):
    if n == 1:
        return 1
    elif n >= 2:
        return f(n-1) + g(n-1) + n


print(sum([int(n) for n in list(str(g(36)))]))

# 40
