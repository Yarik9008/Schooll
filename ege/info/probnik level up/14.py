def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum
mass = []

for x in (1,100000):
    rez = 3 * 16**2018 - 2* 8**1028 - 3*4**1100 - 4**x - 2022
    n = sum([int(a) for a in list(convert(rez,4))])
    if n > 0:
        mass.append(n)

print(len((mass)))
    
# 3