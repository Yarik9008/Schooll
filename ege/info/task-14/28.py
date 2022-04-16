def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

a = 4**1103 + 3*4**1444 - 2*4**144 + 66
print(sum([int(a) for a in list(str(convert(a,4)))]))

# 2882