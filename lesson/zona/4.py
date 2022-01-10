path1 = '/home/proteus/yandex_Hack-1/schooll/zona/file-2/4.3.txt'  # путь до файла

fil = open(path1, 'r')

x, y = [int(i) for i in list(fil.readline().split())]
if x > 1 and y > 1 and y < 3*x + 1 and y < 3*x + 4 and x < 7 or (x == 1 and y == 4):
    print(True)
else:
    print(False)
    
