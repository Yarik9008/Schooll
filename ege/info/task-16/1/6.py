from functools import lru_cache


@lru_cache(maxsize=1000)
def f(n):
    if n > 15:
        return n**2 - 5
    elif n <= 15:
        return n * f(n + 2) + n + f(n + 3)


print(sum([int(n) for n in list(str(f(1)))]))

# 48
