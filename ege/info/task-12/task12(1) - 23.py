stroka = '4' * 86

while '4444' in stroka or '7777' in stroka:
    if '4444' in stroka:
        stroka = stroka.replace('4444', '77', 1)
    elif '777' in stroka:
        stroka = stroka.replace('7777', '44', 1)
    

print(stroka)

# 447744