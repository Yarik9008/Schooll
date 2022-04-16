def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


for i in range(2,10000):
    a = convert(4**2015 + 2**i - 2**2015 + 15, 2)
    if a.count('1') == 500:
        print(i)
        break

# 2510