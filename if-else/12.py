path1 = '/home/proteus/Рабочий стол/Программирование алгоритмов с ветвлением/12.3.txt'  # путь до файла

fil = open(path1, 'r')

mass = [int(i) for i in (fil.readline().split())]

s = list(set(mass))
if mass.count(s[0]) == 1:
    print(mass.index(s[0]) + 1)
else:
    print(mass.index(s[1]) + 1)
    
