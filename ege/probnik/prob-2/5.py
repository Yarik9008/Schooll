for i in range(10000000):
    numbermass = [int(a)for a in list(str(i))]
    sum1 = sum(list(filter(lambda x: x % 2 == 0, numbermass)))
    sum2 = 0
    ch = False
    for e in range(len(numbermass)):
        if ch:
            sum2 += numbermass[e]
            ch = False
        else:
            ch = True
    
    if (sum1 - sum2) == 9:
        print(i)
        break

        

    