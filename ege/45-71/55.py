path1 = '45-71/55.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))
print(ful)
mass = list(filter(lambda x : len(str(oct(x))) - 2 >= 3 and str(oct(x))[-1] == '5', ful))

if len(mass) >0:
    print(max(mass))
else:
    print(0)
    
# 8621
# 0
# 8973