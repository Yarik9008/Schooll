massnumber = {}

for i in range(800000, 10000000):
    massdel = []
    for a in range(1, int(i**0.5)):
        if i % a == 0:
            massdel.append(a)

    if sum(massdel) % 2 == 1:
        out = 1
        for x in massdel:
            out *= x
        if out % 2 == 1:
            if len(massdel) > 10:
                massnumber[i] = massdel
                print(i, len(massdel))

    if len(massnumber) == 6:
        print(massnumber)
        break


