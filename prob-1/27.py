path1 = 'prob-1/data/27-B.txt'  # путь до первого файла
mass = list(map(int, open(path1, 'r').readlines()))

k = 0
s = 0
summass = []
for i in mass:
    s += i
    if i % 2 == 0:
        k += 1
        if k % 10 == 0:
            summass.append(s)
            s = 0


print(max(summass))

# 92759
# 1794363

