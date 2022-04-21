stroka = '1' * 44 + '2' * 21

while '111' in stroka:
    stroka = stroka.replace('111', '2', 1)
    stroka = stroka.replace('22', '1', 1)

print(stroka)

# 212
