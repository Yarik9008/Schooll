
from random import randint
mass = [randint(1, 10000) for i in range(30)]  # формирование массива

print(f'data: {mass}')  # исходные элименты

masspar = []
for i in mass:
    for a in mass:
        if mass.index(a) != mass.index(i):
            masspar.append([i, a])

massminraz = list(map(lambda x: abs(x[0] - x[1]), masspar))
minmass = min(massminraz)
print(f'element: {masspar[massminraz.index(minmass)]}')
print(f'index: {mass.index(masspar[massminraz.index(minmass)][0])}, \
{mass.index(masspar[massminraz.index(minmass)][1])}')

#