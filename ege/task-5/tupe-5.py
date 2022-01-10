# перевод в бинарку 
# если едениц больше то +1 
# если нулей больше то +0
# перевод в десятичную 
num = 0

for i in range(1,1000000):
    bini = str(bin(i)[2:])
    if bini.count('0') <= bini.count('1'):
        bini += '0'
    else:
        bini += '1'
    numb = int(bini, 2)
    
    if numb >= 42:
        break
    else:
        num = numb

print(num)