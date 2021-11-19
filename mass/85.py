path1 = 'schooll/mass/data/85.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

# нахождение кол-во пар
mass1 = ful[:-1]
mass2 = ful[1:]
data = list(zip(mass1, mass2))

massdata = len([sum(a) for a in  list(filter(lambda x: sum(x)  > 0 , data))])
massdata2 = len([sum(a) for a in list(filter(lambda x: sum(x) < 0 , data))])

print(massdata)
print(massdata2)
    

# правильно 