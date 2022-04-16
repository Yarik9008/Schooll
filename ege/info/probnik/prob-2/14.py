a = 3 * 125**6 + 2 * 25**9 + 5**12 - 625


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

print(convert(a, 5).count('0'))