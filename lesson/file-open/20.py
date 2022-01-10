# решение 20 задачи
import math
path1 = '20.1.txt' # путь до первого файла 

fil = open(path1,'r')
fil = float(fil.readline().strip())

print(math.degrees(fil))