a = (729**41 - 81**16)*(729**15 + 9**5)


baze_num = 9


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


print(convert(a, baze_num).count('0'))

# 77
