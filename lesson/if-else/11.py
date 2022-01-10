path1 = '/home/proteus/Рабочий стол/Программирование алгоритмов с ветвлением/11.3.txt'  # путь до файла

fil = open(path1, 'r')

m, n, r = [int(i) for i in (fil.readline().split())]

if n + m > 0:
    print('положтельная')
elif n + r > 0:
    print('положительная')
elif m + r > 0:
    print('положительная')
else:
    print('отрицательная')
    
# +
# - 
# + 

