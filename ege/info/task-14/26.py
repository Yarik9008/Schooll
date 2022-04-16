for i in range(2,10000000):
    a = 64**12 - 8**14 + i
    a = str(oct(a))[2:]
    if a.count('7') == 12 and a.count('1') == 1:
        print(i)
        break


# 127


