
for i in range(1, 20000000):
    num1 = str(bin(i)[2:])
    if i % 2 == 0:
        num1 += '00'
    else: 
        num1 += '11'
    if int(num1, 2) > 115:
        print(i)
        break
