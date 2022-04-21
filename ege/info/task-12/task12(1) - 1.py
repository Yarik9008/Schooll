stroka = '8' * 68

while ('888' in stroka) or ('222' in stroka):
    if '222' in stroka:
        stroka = stroka.replace('222', '8', 1)
    elif '888' in stroka:
        stroka = stroka.replace('888', '2', 1)

print(stroka)

# 28