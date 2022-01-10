path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/9.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if x > 0 and y > 0:
    if x >= 2 and x <= 6:
        if y >= (3 - 1.5 * x) and y < (6 - x):
            print(True)
        else: 
            print(False)
    else:
        print(False)
else:
    print(False)