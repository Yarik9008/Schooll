a = ((44 + 4 ** 50) * 4 ** 25 + 44) * 4 ** 12 + 44

base = 4

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


print(str(convert(a,base).count('0')))

# 81
