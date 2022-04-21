stroka = '1' * 2019 + '3' * 2119

while '11' in stroka:
    stroka = stroka.replace('11', '2', 1)
    stroka = stroka.replace('22', '3', 1)
    stroka = stroka.replace('33', '1', 1)
    

print(stroka)

# 313