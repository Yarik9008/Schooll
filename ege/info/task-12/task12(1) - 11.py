stroka = '7' * 170

while '777' in stroka:
    stroka = stroka.replace('77', '2', 1)
    stroka = stroka.replace('22', '7', 1)

print(stroka)

# 77