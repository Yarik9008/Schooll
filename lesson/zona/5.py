path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/5.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if y > 0 and x > 0:
    if  x**2 + y**2 <= 16:
        print(True)
    else:
        print(False)
elif x > 0 and y <=0:
    if  x**2 + y**2 <= 25:
        print(True)
    else:
        print(False)
else:
    print(False)