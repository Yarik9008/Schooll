# решение 19 задачи
path1 = '19.1.txt'  # путь до первого файла

fil = open(path1, 'r')
fil = fil.readline().strip().split('.')

print('Reverse:',fil[1] + '.' + fil[0])
