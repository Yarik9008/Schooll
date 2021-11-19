path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/2.1.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if x ** 2 + y**2 <= 25 and x ** 2 + y**2 >= 9:
    print(True)
else:
    print(False)
