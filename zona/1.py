path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/1.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if y >= 0 and x>=0 and y < 4 - x:
     print(True)
elif y >= 0 and x <=0 and y < x - 4:
    print(True)
else:
    print(False)