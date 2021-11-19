path1 = '/home/proteus/Рабочий стол/Программирование алгоритмов с ветвлением/10.3.txt'  # путь до файла

fil = open(path1, 'r')

m, n= [int(i) for i in (fil.readline().split())]


et = n // 3 

if et % 2 == 0:
    if et + 1 <= m:
        print(et+1)
    else:
        print(et-1)
else:
    print(et)
    

# 17 
# 5
# 3

