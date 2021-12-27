path1 = '17/17.2/data/17-1.txt'  # путь до первого файла
#path1 = '17/17.2/data/test6.txt'

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

massind = []
for i in range(1, len(ful) - 1):
    if ful[i - 1] > ful[i] and ful[i] < ful[i + 1]:
        massind.append(ful[i]) 


print(len(massind))
print(max(massind))

# 3316
# 8125

# 