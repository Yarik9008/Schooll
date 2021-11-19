path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/13.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if x >= -5 and x <= 5 and y <= 4 and y >= -4:
    print(True)
else:
    print(False)