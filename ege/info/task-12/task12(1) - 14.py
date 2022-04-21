stroka = '1' * 100

while '111' in stroka:
    stroka = stroka.replace('111', '2', 1)
    stroka = stroka.replace('222', '3', 1)
    stroka = stroka.replace('333', '1', 1)

print(stroka)

# 3321