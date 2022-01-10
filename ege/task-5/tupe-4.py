# перевод числа n в бинарку
# сумма всего и остаток в конец
# сумма всего и остаток в конец
# перевод из двоичной в десятичную
param = 0
param2 = 79
mass = []

for i in range(1, 2000000):
    bini = bin(i)[2:]
    bini = str(bini) + str(sum([int(s) for s in list(str(bini))]) % 2)
    bini = str(bini) + str(sum([int(s) for s in list(str(bini))]) % 2)
    num = int(bini, 2)
    if num >= param and num <= param2:
        mass.append(num)

kol = len(set(mass))

print(kol)
