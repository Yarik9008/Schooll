def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

mass = []

for i in range(1,1000):
    a = 7**500 + 7**200 - 7**50 - i
    if a > 0:
        s = sum([int(a) for a in list(str(convert(a,7)))])
        mass.append((s))

print(max(mass))

# 1200