stroka = '687' * 143

while '68' in stroka or '7777' in stroka:
    stroka = stroka.replace('68', '7', 1)
    stroka = stroka.replace('7777', '7', 1)

print(stroka)

# 7