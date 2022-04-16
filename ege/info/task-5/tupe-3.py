kol = 0
for  i in range(1,20000000):
    if i % 2 == 0:
        i /= 2
    else:
        i -= 1
    if i % 7 == 0:
        i /= 7
    else:
        i -= 1
    if i == 2:
        kol += 1


print(kol)