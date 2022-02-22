def f(n):
    if n == 1:
        return 1 
    elif n> 1:
        return 3*f(n-1) + g(n-1) - n + 5 

def g(n):
    if n == 1:
        return 1
    elif n> 1:
        return f(n-1) + 3*g(n-1) - 3*n
    


print(f(14) + g(14))

# 37282721
