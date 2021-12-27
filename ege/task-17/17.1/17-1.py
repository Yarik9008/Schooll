path1 = '/17/17.1/data/17-4.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

otv = []

for i in ful:
    kol = 0 
    for a in [2,3,5,7]:
        if i % a == 0:
            kol += 1
    if kol == 2:
        otv.append(i)
        
print(len(otv))
print(min(otv) + max(otv))

#531
#10774

# правильно