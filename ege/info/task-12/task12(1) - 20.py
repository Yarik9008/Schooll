stroka = '7' + '8' * 55

while '78' in stroka or '7' in stroka:
    if '788' in stroka:
        stroka = stroka.replace('78', '8887', 1)
    elif '7' in stroka:
        stroka = stroka.replace('7', '8888', 1)
    

print(stroka.count('8'))

# 167