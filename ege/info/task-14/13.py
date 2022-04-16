mass = []
num = 609


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


for i in range(2, 11):
    number = convert(num, i)
    if (int(str(number)[0]) % 2 == 0 and int(str(number)[-1]) % 2 == 0) or (int(str(number)[0]) % 2 == 1 and int(str(number)[-1]) % 2 == 1):
        continue
    else:
        mass.append(i)

print(sum(mass))

# 36 

