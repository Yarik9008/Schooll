# решение 18 задачи
import time
path1 = '18.1.txt'  # путь до первого файла

fil = open(path1, 'r')
fil = int(fil.readline().strip())

tim = time.strftime('%H:%M:%S', time.gmtime(fil))

print('Time:', tim)
