path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/10.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if x >= 0 and y >= 0:
    if x ** 2 + y ** 2 <= 36 and  y > 3 - x:
        print(True)
    else:
        print(False)
else:
    print(False)