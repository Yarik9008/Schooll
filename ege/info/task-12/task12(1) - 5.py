stroka = '1' * 99 

while '111' in stroka:
    stroka = stroka.replace('111', '22', 1)
    stroka = stroka.replace('222', '11', 1)

print(stroka)

# 221
