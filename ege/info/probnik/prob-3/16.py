from functools import lru_cache


@lru_cache()
def f(n):
    if n == 0:
        return 0 
    elif n % 2 == 1:
        return f(n-1) + 1
    elif n > 0 and n % 2 == 0:
        return f(n/2)

kol = 0 
for i in range(1000000000):
    if f(i) == 2:
        kol += 1
        #print(1)

print(kol)