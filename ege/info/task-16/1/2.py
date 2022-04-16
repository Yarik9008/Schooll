from functools import lru_cache


@lru_cache(maxsize=1000)
def f(n):
    if n <= 3:
        return 3
    elif n > 3 and n <= 32:
        return n // 4 + f(n-3)
    elif n > 32:
        return 2 * f(n-5)


print(f(100))

# 655360
