for i in range(200000000):
    i = str(i) + str(i)[-1]
    num1 = str(bin(int(i))[2:])
    num1 += str(num1.count('1') % 2)
    num2 = int(num1, 2)
    if num2 > 413:
        print(i)
        break