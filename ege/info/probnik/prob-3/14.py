a  = 5*343**8 + 4*49**12 + 7**14 - 98

baze_num = 7

def convert(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

a = convert(a,baze_num)

for i in set(list(str(a))):
    print(i, ' -- ', str(a).count(i))