'''
a = bin(123)[2:] # перевод из десятичной в двоичную
print(a)

b = int('10010101010110', 2) # перевод из двоичной или любой другой в десятичную
print(b)

c = int([object]) # [основание системы счисления]) - преобразование к целому числу в десятичной системе счисления. По умолчанию система счисления десятичная, но можно задать любое основание от 2 до 36 включительно.
d = bin() # преобразование целого числа в двоичную строку.
e = hex() # преобразование целого числа в шестнадцатеричную строку.
f = oct() # преобразование целого числа в восьмеричную строку.
'''
print(['0'] * (6 - 1))