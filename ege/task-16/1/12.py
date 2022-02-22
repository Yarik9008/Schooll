from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
    if n <= 13:
        return n**3 + n**2 + 1
    elif n % 3 == 0:
        return f(n-1) + 2*n*n -3
    elif n%3 != 0:
        return f(n-2) + 3*n + 6 

kol = 0
mass = ['2','4','6','8', '0']
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

# 14 