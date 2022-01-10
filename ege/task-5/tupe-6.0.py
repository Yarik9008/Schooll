# последняя еденица не инвертируется и нули стоящие после нее 
number = 98
num1 = str(bin(number)[2:])
numrev = num1
numrev = numrev[::-1]

sr = num1[: -(numrev.index('1')+1)]
sr3 = num1[-(numrev.index('1')+1):]
sr2 = ''
for i in list(sr):
    if i == '0':
        sr2 += '1'
    else:
        sr2 += '0'

sr2 += sr3

print(int(sr2, 2))

