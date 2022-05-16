data  = 5 * 729 ** 8 + 7 * 81 ** 12 + 3 ** 16 - 171

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

kol  = 0 
print(convert(data, 9))
for i in list(str(convert(data, 9))):
    if int(i) % 2 == 0:
        kol += 1 

print(kol)