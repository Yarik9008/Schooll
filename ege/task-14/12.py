mass = []
num = 456

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

for i in range(2,11):
    number = convert(num,i)
    kol = 0
    for d in list(str(number)):
        if int(d) % 2 == 1:
            kol += 1
    mass.append([i,number,kol])

print(max(mass, key=lambda x: x[2]))
print(mass)

# 5 

