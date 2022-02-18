from functools import lru_cache


@lru_cache(maxsize=1000)
def f(n):
    if n > 25:
        return 2*(n**3) + 1
    elif n <= 25:
        return f(n+2) + 2*f(n+3)


kol = 0
for i in range(1, 1001):
    if f(i) % 11 == 0:
        kol += 1

print(kol)


# 91
