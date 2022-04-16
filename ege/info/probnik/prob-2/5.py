for i in range(10000000):
    numbermass = [int(a)for a in list(str(i))]
    sum1 = sum(list(filter(lambda x: x % 2 == 0, numbermass)))
    sum2 = sum([int(i) for i in ([0] + list(str(i)))[::2]])
    if abs(sum1 - sum2) == 9:
        print(i)
        break

        

    