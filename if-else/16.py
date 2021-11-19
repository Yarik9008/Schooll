path1 = '/home/proteus/Рабочий стол/Программирование алгоритмов с ветвлением/16.3.txt'  # путь до файла

fil = open(path1, 'r')

ax1, ay1 = [int(i) for i in (fil.readline().split())]
x1, y1, x2, y2, x3, y3 = [int(i) for i in (fil.readline().split())]

k1 = (y1 - y2) / (x1 - x2)
b1 = y2 - k1 * x2

k2 = (y2 - y3) / (x2 - x3)
b2 = y3 - k2 * x3

k3 = (y3 - y1) / (x3 - x1)
b3 = y1 - k3 * x1 

if ax1 * k1 + b1 == ay1:
    print('лежит')
elif ax1 * k2 + b2 == ay1:
    print('лежит')
elif ax1 * k3 + b3 == ay1:
    print('лежит')
else:
    print('не лежит')
    
# не лежит 
# лежит 
# лежит 

