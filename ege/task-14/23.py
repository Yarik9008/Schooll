num = 437
mass = []


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


for i in range(2, 11):
    number = convert(num,i)
    

print(sum(mass))