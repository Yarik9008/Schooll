path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/17.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]

if x >= 0 and y >= 0 and x <= 6 and x >= -6 and y <= 5 and y >= -5:
    if x ** 2 + y ** 2 <= 36:
        print(True)
    else:
        print(False)
elif x < 0 and y > 0 and x <= 6 and x >= -6 and y <= 5 and y >= -5:
    if y < (6 - x):
        print(True)
    else:
        print(False)
elif x < 0 and y < 0 and x <=6 and x >= -6 and y <= 5 and y >= -5: 
    if  y > x - 6:
        print(True)
    else:
        print(False)
else:
    print(False)
