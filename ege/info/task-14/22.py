num = 430
mass = []


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


for i in range(2, 11):
    number = convert(num,i)
    sr1 = ''.join(sorted(list(str(number)), reverse=True))
    if str(number) == sr1:
        mass.append((i))

print(sum(mass))

# 15 
