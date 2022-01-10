path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/3.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if y >=0 and y <= 4 and x >=-2 and x <= 2:
    print(True)
elif y < 0 and x <= 5 and x >= -5 and  y >= -3:
    print(True)
else:
    print(False)