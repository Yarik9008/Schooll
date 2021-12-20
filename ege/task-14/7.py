def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

baze_num = 8
mass = []

for i in range(4,9):
    a = (88 + 2*8**i)*8**i + 88 + 8**8
    mass.append(sum([int(s) for s in str(convert(a,baze_num))]))


print(mass)
# 11 
