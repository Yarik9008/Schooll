path1 = '17/17.2/data/17-2.txt'

mass = open(path1, 'r').readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

print(ful.count(max(ful)))
print(ful.index(max(ful)) + 1)

# 9
# 26 

#

