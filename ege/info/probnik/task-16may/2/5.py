kol = 0

for i in range(1,99999999):
    num = sum([int(a) for a in list(str(i))])
    
    num = str(bin(num))[2:]
    if num.count('1') % 2 == 0:
        num = '1' + num + '00'
    else:
        num = '10' + num + '1'
    if int(num,2) == 21:
        kol += 1

print(kol)
# num = str(bin(456))[3:]
# print(num)
# print(bin(456))

# 36
