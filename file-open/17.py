# решение 17 задачи
import math
path1 = '17.1.txt'  # путь до первого файла

fil = open(path1, 'r')
fil = fil.readline().split()
n, r = [float(i) for i in fil]
# вычисление площади по формуле
s = r**2 * n * math.tan(180 / n)

print('S =', s)
