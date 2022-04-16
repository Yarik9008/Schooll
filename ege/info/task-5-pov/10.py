kol = 0

for i in range(2,100000000):
    num = str(bin(i))[2:]

    if num.count('1') > num.count('0'):
        num += '0'
    else:
        num += '1'

    if len(num) % 2 == 0:
        num = num[:len(num) // 2 - 1] + num[len(num) // 2 +1:]
    else:
        num = num[:len(num) // 2 - 1] + num[len(num) // 2 + 1:]
    
    #print(num)
    if int(num, 2) == 58:
        kol += 1 


print(kol)

