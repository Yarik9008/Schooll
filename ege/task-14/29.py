def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

a = 81**18 - (81**8 - 1)*((8 + 1)**8 + 1) / 8 - 8
print(convert(a,3).count('1'))

# 17 


