for i in range(100000000):
    num = str(bin(i))[2:]
    if num.count('1') > num.count('0'):
        num += '0'
    else:
        num = '11' + num
    if num.count('1') > num.count('0'):
        num += '0'
    else:
        num = '11' + num
    
    if int(num, 2) > 500:
        print(i)
        break
# 32
