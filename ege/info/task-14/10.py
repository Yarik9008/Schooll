mass = []
num = 1234

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

for i in range(2,11):
    mass.append(sum([int(s) for s in list(str(convert(num,i)))]))

print(mass)

# 6 