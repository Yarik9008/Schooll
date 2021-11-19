path1 = 'schooll/mass/data/84.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

kol = 0 
sk = 0
ma = []
for i in ful:
    if str(hex(i))[-1] == str(oct(i))[-1]:
        kol += 1
        ma.append(sk)
    sk += 1

print(kol)
print(ma)

# 5
# 16
# 11
# правильно 