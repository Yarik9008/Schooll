stroka = '1' * 90

while '1111' in stroka or '0000' in stroka:
    if '1111' in stroka:
        stroka = stroka.replace('1111', '10000', 1)
    elif '000' in stroka:
        stroka = stroka.replace('000', '11', 1)
    

print(stroka.count('1'))

# 68