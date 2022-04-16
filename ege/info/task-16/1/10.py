from functools import lru_cache


@lru_cache(maxsize=1000)
def f(n):
    if n > 25:
        return n ** 2 + 2*n + 1
    elif n%2 == 0:
        return 2 * f(n + 1) + f(n + 3)
    elif n % 2 != 0:
        return f(n+2) + 3*f(n+5)



kol = 0
for i in range(1, 1001):
    if '0' not in str(f(i)):
        kol += 1


print(kol)

# 575