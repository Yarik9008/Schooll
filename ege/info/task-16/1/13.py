from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
    if n <= 5:
        return n + 15 
    elif n % 2 == 0:
        return f(n//2) + n**3 - 1
    elif n % 2 == 1:
        return f(n-1) + 2*n**2  + 1

kol = 0
for i in range(1,1001):
    if str(f(i)).count('8') >= 2:
        kol += 1
    
print(kol)

# 164