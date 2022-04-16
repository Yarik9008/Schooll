mass = sorted(list('aoy'), reverse=True)
kol = 0
for a1 in mass:
    for a2 in mass:
        for a3 in mass:
            for a4 in mass:
                for a5 in mass:
                    kol += 1
                    sl = a1+a2+a3+a4+a5
                    if kol == 240:
                        print(sl)

# aaaoa
