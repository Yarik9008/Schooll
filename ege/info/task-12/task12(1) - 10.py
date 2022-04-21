stroka = '1' * 198

while '1111' in stroka:
    stroka = stroka.replace('1111', '33', 1)
    stroka = stroka.replace('333', '1', 1)

print(stroka)

# 13
