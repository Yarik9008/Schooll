for i in range(2,100):
    a = 36**17 - 6**i + 71
    d = str(hex(a))[2:]
    kol = 0
    for f in list(d):
        try:
            kol += int(f)
        except:
            continue
    if kol == 61:
        print(i)
        break

# 27