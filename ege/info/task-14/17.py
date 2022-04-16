num = 8040
mass = []


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


for i in range(2, 11):
    number = convert(num,i)
    if '2' not in str(number):
        mass.append((i))

print(sum(mass))

# 20

