for i in range(1000000000):
    num = str(bin(i))[2:]
    if i % 2  == 0:
        num = '1' + num
    else:
        num += '0'
    
    if num.count('1') % 2 == 0:
        num += '1'
    else:
        num += '0'
    
    if int(num, 2) > 228:
        print(i)
        break

# 50
