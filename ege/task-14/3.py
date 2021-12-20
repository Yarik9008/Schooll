a = (2 * 343 ** 123 + 2401)*(3 * 343 ** 137 - 2401)


baze_num = 7


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


print(convert(a, baze_num).count('6'))

# 407 
