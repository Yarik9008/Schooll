for i in range(1000000):
    qwe = i
    i = i // 10
    n = 1
    while i < 221:
        if n % 2 ==0:
            i += 13
        n +=  5
    if n == 101:
        print(qwe)
        
        