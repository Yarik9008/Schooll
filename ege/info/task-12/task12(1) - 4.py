stroka = '2' * 3 + '5' * 18

while '222' in stroka or '888' in stroka:
    
    while '555' in stroka:
        stroka = stroka.replace('555', '8', 1 )
    
    if '222' in stroka:
        stroka = stroka.replace('222', '8', 1 )
    elif '888' in stroka:
        stroka = stroka.replace('888', '2', 1)



print(stroka)

# 228 
