a = (66+6**2019)*6**2019 + 66 + 6**6

base = 6


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


print(sum([int(i) for i in list(str(convert(a, base)))]))

# 14
