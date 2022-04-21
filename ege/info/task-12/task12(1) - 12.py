stroka = '561' * 102

while '56' in stroka or '1111' in stroka:
    stroka = stroka.replace('56', '1', 1)
    stroka = stroka.replace('1111', '1', 1)

print(stroka)

# 111