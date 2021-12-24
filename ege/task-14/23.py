num = 437
mass = []


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

def chech_simple(num):
    kol = 0
    for i in range(2,num):
        if num % i == 0:
            kol += 1
    if kol == 0:
        return True
    else:
        return False


for i in range(2, 11):
    number = convert(num,i)
    num2 = sum([int(d) for d in list(str(number))])
    if chech_simple(num2):
        mass.append(i)

print(sum(mass))

# 33 
