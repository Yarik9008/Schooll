from functools import lru_cache


@lru_cache(maxsize=1000)
def f(n):
    if n > 20:
        return n**3 + n
    elif n % 2 == 0:
        return 3*f(n+1) + f(n+3)
    elif n % 2 == 1:
        return f(n+2) + 2*f(n+3)


kol = 0
for i in range(1, 1001):
    if '1' not in str(f(i)):
        kol += 1
print(kol)

# 384