file  = open('C:/Users/Yarik9008/YandexDisk/Schooll/ege/info/task-24/data/24-2.txt')
s = file.readlines()

mass_g = []
for i in range(len(s)):
    mass_g.append(s[i].count('G'))

min_g = s[mass_g.index(min(mass_g))]

mass_sim = {}
for i in range(len(min_g)):
    sim = min_g[i]
    mass_sim[sim] = min_g.count(sim)
print(mass_sim)
'''
'T': 50
'D': 50
'''
print(sorted('TD'))

# T