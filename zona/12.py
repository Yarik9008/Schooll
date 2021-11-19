path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/12.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if x >= 0:
    if y >= 0 and y ** 2 + x ** 2 <= 36:
        print(True)
    elif y < 0 and y > 6 - x:
        print(True)
    else: 
        print(False)
else:
    print(False)