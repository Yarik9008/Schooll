path1 = '8.3.txt'  # путь до файла

fil = open(path1, 'r')

a, b = [int(i) for i in list(fil.readline().split())]
x, y, z = [int(i) for i in list(fil.readline().split())]

if (a <= x and b <= y) or (b <= x and a <=y): #проверка х-у
    print('пройдет')
elif (a <= y and b <= z) or (a <= z and b <= y): #проверка по y-z
    print('пройдет')
elif (a <=x and b <= z) or (b <= x and a<= z): #проверка по x-z
    print('пройдет')
else: 
    print('не пройдет')
