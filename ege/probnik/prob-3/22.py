for i in range(110, 150):
    x = i
    a,b = 0,0
    while x > 0:
        a += 1
        if x % 2 == 0:
            b += x % 100
    x //= 10
    print()
    if a == 4 and b == 142:
        print(i)
           