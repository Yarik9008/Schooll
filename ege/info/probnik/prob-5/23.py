def f(n, check):
    if n == 12 and check:
        return 1

    elif n < 12:
        return 0 
    
    elif n == 42:
        check = True
    
    return f(n -2, check) + f(n // 2, check)

print(f(108, False))