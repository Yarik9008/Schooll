databaze = {10:'№', 11:'#',12:'@',13:'$', 14:'*'}

def convert(num, base):
    newNum = ''
    while num > 0:
        a = num % base
        if a > 9:
            a = databaze[a]
        else:
            a = str(a)
        newNum = a + newNum
        num //= base
    return newNum

a = 100**2 + 625**25 + 5**100
print(str(convert(a, 15)).count('@'))

# 3 
