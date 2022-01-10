path1 = 'schooll/mass/data/39.1.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

ful1 = ful[:len(ful) // 2]
ful2 = ful[len(ful) // 2:][::-1]

data = list(zip(ful1,ful2))
print(len(list(filter(lambda x: x > 20, [sum(i) for i in data]))))

# 9 
# 18
# 1

# правильно 