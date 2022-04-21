stroka = '1' * 95 + '7' * 31

while '1111' in stroka:
    stroka = stroka.replace('1111', '7', 1)
    stroka = stroka.replace('77', '1', 1)


print(stroka)

# 717