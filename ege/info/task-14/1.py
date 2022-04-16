a  = 7*6561**46 + 8*729**15 - 6*5832

baze_num = 9

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

print(convert(a,baze_num).count('7'))

# 2 
