for i in range(1000000):
    if i % 2 ==0:
        num = '11' + str(bin(i))[2:] + '11'
    else:
        num = '1' + str(bin(i))[2:] + '0'
    if int(num, 2) < 126:
        print(int(num, 2))

# 122
