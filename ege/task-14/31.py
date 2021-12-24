a = (7**160 * 7**90) - (14**150 + 2**13)
def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum
kol = 0
for i in list(str(convert(a,7))):
    i = int(i)
    if i != 6:
        kol += i

print(kol)

# 145
