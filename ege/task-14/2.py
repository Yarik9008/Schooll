a = 5*6561**46 + 5*729**15 - 5*5832 - 5 


baze_num = 9

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

print(convert(a,baze_num).count('4'))

# 4
