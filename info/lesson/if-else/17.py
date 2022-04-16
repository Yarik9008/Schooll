from math import atan,pi
path1 = 'schooll/if-else/Программирование алгоритмов с ветвлением/17.3.txt'  # путь до файла

fil = open(path1, 'r')

a1, b1, c1  = [int(i) for i in (fil.readline().split())]
a2, b2, c2 = [int(i) for i in (fil.readline().split())]

if (a1 * a2 + b1 * b2) == 0:
    print('перпендикулярны')
else:
    alfa = round(atan((a1*b2 - a2*b1) / (a1*a2 + b1 * b2))* 180 / pi, 3)
    print('прямые не перпендикулятрны, угол: ',alfa)

# прямые не перпендикулятрны, угол:  -45.0
# прямые не перпендикулятрны, угол:  29.745
# прямые не перпендикулятрны, угол:  60.255
