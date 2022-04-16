def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

for i in range(2,1001):
    a = i**25 - 2*i**13 + 10
    a = convert(a,i)
    if sum([int(s) for s in list(str(a))]) == 75:
        print(i)
        break
    else:
        print('no')

# 7
