from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
    if n <= 3:
        return n 
    elif n % 2 == 0: 
        return 2*n*n + f(n-1)
    elif n % 2 == 1:
        return n**3 + n + f(n-1) 

for i in range(10**7):
    if f(i) >= 10**7:
        print(i)
        break

# 93