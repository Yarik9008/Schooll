# решение 16 задачи
import math
path1 = '16.1.txt'  # путь до первого файла

# считываем строку и преобразовываем ее в список чисел
fil = open(path1, 'r')
fil = [int(i) for i in list(str(fil.readline().strip()))] 
# произведение всех элиментов массива  
proiz = math.prod(fil)

print('Proiz =', proiz)
