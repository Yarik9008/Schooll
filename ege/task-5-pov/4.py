kol = 0
for i in range(1, 10000000):
    num = sum([int(i) for i in list(str(bin(1)[2:]))])
    ost = num % 2
    num = str(num) + str(ost)
    if [int(i) for i in list(str(bin(i)[2:]))].count('1') > [int(i) for i in list(str(bin(i)[2:]))].count('0'):
        num += '0'
    else:
        num += '1'
    
    num = int(num,2)
    if num >= 50 and num <= 80:
        kol += 1
    
print(kol)
 
# 7 