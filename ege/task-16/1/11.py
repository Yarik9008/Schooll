from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
    if n <= 15:
        return n ** 2 + 3 * n + 9 
    elif n % 3 == 0:
        return f(n-1) + n - 2  
    elif n % 3 != 0:
        return f(n-2) + n + 2


kol = 0
mass = ['1','3','5','7','9']
for i in range(1,1001):
    check_out = False
    out = str(f(i))
    for a in mass:
        if a in out:
            check_out = True
            break
    if not check_out:
        kol += 1

print(kol)

# 33