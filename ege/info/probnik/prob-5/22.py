for i in range(1,1000):
    x = i
    k = 9 * x - 57
    d = 9 * x + 13 
    while k*d > 0:
        if k > d:
            k = k % d
        else:
            d = d % k
    if k+d == 70:
        print(i)