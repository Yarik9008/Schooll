file = open('C:/Users/Yarik9008/YandexDisk/Schooll/ege/info/probnik/prob-5/24.txt')
data = file.readline()

while 'CACAC' in data:
    data = data.replace('CACAC', 'CACCAC')

data = data.replace('AB', '11')
data = data.replace('CAC', '111')

masscol = []
tek = 0

for i in range(len(data)):
    if data[i] == '1':
        tek += 1
    else:
        if tek != 0:
            masscol.append(tek)
            tek = 0

print(max(masscol))