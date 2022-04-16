path1 = '9.3.txt'  # путь до файла

fil = open(path1, 'r')

x1, y1, x2 = [int(i) for i in list(fil.readline().split())]
x3, y3, x4 = [int(i) for i in list(fil.readline().split())]

if x1 <= x3 and x3 <= x2 and x2 <= x4:
    print((x2 - x3) * (y3 - (y3 - y1)))
elif x3 <= x1 and x1 <= x4 and x4 <= x2:
    print((x4-x1) * (y1 - (y1 - y3)))
else:
    print('не пересекает')
