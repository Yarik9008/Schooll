stroka = '1' * 2018 + '3' * 2050

while '111' in stroka:
    stroka = stroka.replace('111', '2', 1)
    stroka = stroka.replace('222', '3', 1)
    stroka = stroka.replace('333', '1', 1)
    
stroka = sum([int(i) for i in list(stroka)])


print(stroka)

# 13