def f(n):
    print(n+1)
    if n > 1:
        print(2*n)
        f(n-1)
        f(n-3)

