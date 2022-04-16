for i in range(20000000):
    num1  = str(bin(i)[2:])
    if num1.count('1') > num1.count('0'):
        num1 += '0'
    else:
        num1 = '11' + num1
    
    if num1.count('1') > num1.count('0'):
        num1 += '0'
    else:
        num1 = '11' + num1
    num2 = int(num1, 2)
    if num2 > 500:
        print(i)
        break
    
