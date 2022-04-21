stroka = '8' * 70

while '2222' in stroka or '8888' in stroka:
    if '2222' in stroka:
        stroka = stroka.replace('2222', '88', 1)
    elif '8888' in stroka:
        stroka = stroka.replace('8888', '22', 1)

print(stroka)

# 22
