from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
    if n <= 3:
        return n 
    elif n % 2 == 0: 
        return f(n-1) + 2*f(n/2)
    elif n % 2 == 1:
        return f(n-1) + f(n-3) 

for i in range(1, 10**8):
    if f(i) >= 10**8:
        print(i)
        break

# 65