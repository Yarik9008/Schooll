num = 1988
mass = []


def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


for i in range(2, 11):
    ch = True
    number = convert(num,i)
    mass1 = str(number)[:-1]
    mass2 = str(number)[1:]
    data = list(zip(mass1, mass2))
    for d in data:
        if len(set(d)) == 1:
            print(len(set(d)))
            ch = False
            print('no')
            continue
    if ch:
        print(data)
        mass.append(i)

print(sum(mass))

# 22

