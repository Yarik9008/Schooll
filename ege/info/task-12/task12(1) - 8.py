stroka = '1' * 50 + '2' * 50 + '3' * 50 

while '12' in stroka or '32' in stroka or '31' in stroka:
    if '12' in stroka:
        stroka = stroka.replace('12', '21', 1)

    if '32' in stroka:
        stroka = stroka.replace('32', '23', 1)

    if '31' in stroka:
        stroka = stroka.replace('31', '13', 1)


print(stroka[19] + stroka[79] + stroka[119])

# 213
