stroka = '1'  + '2' * 51

while '12' in stroka or '1' in stroka:
    if '12' in stroka:
        stroka = stroka.replace('12', '2221', 1)
    elif '1' in stroka:
        stroka = stroka.replace('1', '222222', 1)
    

print(stroka.count('2'))

# 159