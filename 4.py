number = (2 * 343**123 + 2401) * (3 * 343**137 - 2401)

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


print(str(convert(number, 7)).count('6'))