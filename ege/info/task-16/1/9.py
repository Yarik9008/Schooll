from functools import lru_cache
import re


@lru_cache(maxsize=1000)
def f(n):
    if n > 25:
        return n**2 + 4*n + 3
    elif n % 3 == 0 and n <= 25:
        return f(n+1) + 2*f(n+4)
    elif n % 3 != 0 and n <= 25:
        return f(n+2) + 3*f(n+5)


kol = 0
for i in range(1, 1001):
    if sum([int(n) for n in list(str(f(i)))]) == 24:
        kol += 1


print(kol)

# 100