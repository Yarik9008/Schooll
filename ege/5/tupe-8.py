
for i in range(1, 20000000):
    num1 = str(bin(i)[2:])
    num1 += num1[-1]
    num1 += str(num1.count('1') % 2)
    num1 += str(num1.count('1') % 2)
    
    if int(num1, 2) > 80:
        print(i)
        break
