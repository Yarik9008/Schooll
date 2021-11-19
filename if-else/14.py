from math import atan

path1 = '/home/proteus/Рабочий стол/Программирование алгоритмов с ветвлением/14.3.txt'  # путь до файла

fil = open(path1, 'r')

x1, y1 = [int(i) for i in (fil.readline().split())]
x2, y2 = [int(i) for i in (fil.readline().split())]
x3, y3 = [int(i) for i in (fil.readline().split())]
x4, y4 = [int(i) for i in (fil.readline().split())]

a = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 3)
b = round(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5, 3)
c = round(((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5, 3)
d = round(((x1 - x4) ** 2 + (y1 - y4) ** 2) ** 0.5, 3)

if x3 - x4 != 0:
    k1 = (y3 - y4) / (x3 - x4)
else:
    k1 = 0

if x1 - x4 != 0:
    k2 = (y1 - y4) / (x1 - x4)
else:
    k2 = 0 

alfa= atan((k2 - k1) / (1 + k1 * k2))

if len(set([a,b,c,d])) == 1 and alfa == 0:
    print('квадрат')
elif len(set([a, b, c, d])) == 1 and alfa != 0:
    print('ромб')
elif len(set([a, b, c, d])) == 2 and alfa == 0:
    print('прямоугольник')
elif len(set([a, b, c, d])) == 2 and alfa != 0:
    print('парралелаграмм')

'''
квадрат
ромб
парралелограмм
'''
