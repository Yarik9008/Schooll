mass = []


for i in range(256):
    num = str(bin(i))[2:]
    num2 = num[::-1]
    rez = int(num,2) - int(num2,2)
    mass.append(rez)

print(max(mass))

# 225
