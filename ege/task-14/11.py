mass = []
num = 3456

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

for i in range(2,11):
    mass.append([i, convert(num,i)])

print(mass)

# 23 
