for i in range(20000000):
    num1 = str(bin(i)[2:])
    if i % 2 == 1:
        num1 += '0'
    else:
        num1 += '1'
    num1 += str(1 - num1.count('1') % 2)
    num2 = int(num1, 2)
    if num2 > 228:
        print(i)
        break
    