stroka = '7' * 120

while '88777' in stroka or '7' in stroka:
    if '88777' in stroka:
        stroka = stroka.replace('88777', '8', 1)
    elif '7' in stroka:
        stroka = stroka.replace('7', '8', 1)
    

print(stroka)

# 8888