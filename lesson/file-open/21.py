# решение 21 задачи
path1 = '15.1.txt'  # путь до первого файла

fil = open(path1, 'r')
fil = float(fil.readline().strip())

h = fil // 6
m = ((fil / 6) % 1 * 60) // 1

print('h:', h, 'm:', m)
