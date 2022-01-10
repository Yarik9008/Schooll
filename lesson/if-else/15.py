path1 = '/home/proteus/Рабочий стол/Программирование алгоритмов с ветвлением/15.2.txt'  # путь до файла
2
fil = open(path1, 'r')

a1, a2 = [int(i) for i in (fil.readline().split())]

s1 = a1 ** 2 * 3 ** 0.5
s2 = a2 ** 2 * 3 ** 0.5

if s1 == s2:
    print('площади равны')
elif s1 > s2:
    print('первая', s1 - s2)
elif s2 > s1:
    print('вторая', s2 - s1) 

# 76,21
# 50,22
# равны 