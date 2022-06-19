file = open('C:/Users/Yarik9008/YandexDisk/Schooll/ege/info/task-24/data/24.txt')
s = file.readline()
while 'CACAC' in s:
    s = s.replace('CACAC', 'CACCAC')

s = s.replace('AB', '11')
s = s.replace('CAC','111')

mass = []
tek  = 0
for i in range(len(s)):
    sim = s[i]
    if sim == '1':
        tek += 1
    else:
        if tek != 0:
            mass.append(tek)
            tek = 0

print(max(mass))
