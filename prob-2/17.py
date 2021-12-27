path1 = 'prob-2/17.txt'  # путь до первого файла
mass = [int(i.split()[0]) for i in  open(path1, 'r').readlines()]

sred = list(filter(lambda x: x % 2 == 0, mass))
sred = sum(sred) / len(sred)

mass1 = mass[:-1]
mass2 = mass[1:]
data = list(zip(mass1, mass2))

data = list(filter(lambda x: (x[0] % 3 == 0 or x[1] % 3 == 0) and (( sred > x[0]) or  ( sred > x[1])), data))

print(len(data))

maxi = list(map(lambda x: x[0] + x[1], data))

print(max(maxi))