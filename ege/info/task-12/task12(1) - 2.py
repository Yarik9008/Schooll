stroka = '1' + '8'*80

while '18' in stroka or '288' in stroka or '3888' in stroka:
    if '18' in stroka:
        stroka = stroka.replace('18', '2', 1)
    elif '288' in stroka:
        stroka = stroka.replace('288', '3', 1)
    elif '3888' in stroka:
        stroka = stroka.replace('3888', '1', 1)


print(stroka)

# 28 
