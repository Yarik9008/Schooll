mass = sorted(list('дейкстра'))
mass3 = 'дйкстр'
kol = 0
mass2 = []
for a1 in mass:
    for a2 in mass:
        for a3 in mass:
            for a4 in mass:
                for a5 in mass:
                    for a6 in mass:
                        sl = a1+a2+a3+a4+a5+a6
                        if sl.count('й') == 1:
                            try:
                                if sl[sl.index('й') + 1] in mass3:
                                    kol += 1
                            except:
                                kol += 0

print(kol)

# 60025

