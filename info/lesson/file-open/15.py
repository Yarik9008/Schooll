# решение 15 задачи
path1 = '15.1.txt' # путь до первого файла 

fil = open(path1, 'r')
fil = fil.readline().split()
x1, y1, x2, y2, x3, y3 = [float(i) for i in fil]

a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 # вычисление 3 сторон 
b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

p = a + b + c
s = abs(0.5 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)))

print('P =', a + b + c)
print('S =', s)
