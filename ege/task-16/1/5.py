from functools import lru_cache


@lru_cache(maxsize=1000)
def f(n):
    if n <= 3:
        return n 
    elif n % 2 == 0: 
        return 2*n + f(n-1)
    elif n % 2 == 1:
        return n**2 + f(n-2) 


kol = 0
for i in range(1,101):
    if f(i) % 3 == 0:
        kol += 1
        
print(kol)

# 32
