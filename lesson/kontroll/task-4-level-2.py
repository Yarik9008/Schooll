path1 = 'kontroll/data/КР5-3.txt'


mass = open(path1, 'r').readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

#print('input: ', *ful)

massiv = list(map(lambda x: sum([int(i) for i in list(str(x))]), ful))
pl = ful[massiv.index(max(massiv))]
print('element: ', pl)
out = [i + pl if len(str(oct(i))) == 4 else i for i in ful]
print('output: ', out)

# правильно
