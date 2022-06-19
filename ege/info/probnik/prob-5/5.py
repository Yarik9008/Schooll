mass = []
for i in range(1, 10000000):
    num = str(bin(i))[4:]
    if num.count('1') % 2 == 0:
        num = '10'+num
    else:
        num = '1' + num + '0'
    if int(num,2) < 450:
        mass.append(int(num,2))

print(max(mass))


