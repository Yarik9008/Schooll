

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

a = 7**103 + 6*7**104 - 3*7**57 + 98
print(sum([int(a) for a in list(str(convert(a,7)))]))

# 282 
