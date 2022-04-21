stroka = '1' * 2019 + '2' * 2019

while '222' in stroka:
    stroka = stroka.replace('222', '1', 1)
    stroka = stroka.replace('111', '2', 1)
    

print(stroka)

# 21