for s in range(10000):
    a = s
    s =  s // 7
    n = 1
    while s < 255:
        if (s + n) % 2 == 0:
            s += 11
        n += 5 
    if n == 106:
        print(a)
        break
    