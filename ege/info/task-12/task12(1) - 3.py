stroka = '4' * 9 + '5' * 12

while '444' in stroka or '888' in stroka:
    if '444' in stroka:
        stroka = stroka.replace('444', '8', 1)
    
    while '555' in stroka:
        stroka = stroka.replace('555', '8', 1 )
    
    while '888' in stroka:
        stroka = stroka.replace('888', '3', 1 )



print(stroka)

# 338 
