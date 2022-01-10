number = 143

num1 = list(str(bin(number)[2:]))
num2 = ''
for i in num1:
    if i == '0':
        num2 += '1'
    else:
        num2 += '0'

print(int(num2, 2) + 1)
    