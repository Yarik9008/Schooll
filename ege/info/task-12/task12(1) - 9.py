stroka = '1' * 50 + '2' * 50 + '3' * 50 

while '13' in stroka or '32' in stroka or '12' in stroka:
    if '13' in stroka:
        stroka = stroka.replace('13', '31', 1)

    if '32' in stroka:
        stroka = stroka.replace('32', '23', 1)

    if '12' in stroka:
        stroka = stroka.replace('12', '21', 1)


print(stroka[9] + stroka[69] + stroka[139])

# 231
