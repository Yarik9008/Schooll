mass = list('мимикрия')
mass2 = []
for a1 in mass:
    for a2 in mass:
        for a3 in mass:
            for a4 in mass:
                for a5 in mass:
                    for a6 in mass:
                        for a7 in mass:
                            for a8 in mass:
                                sl  = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
                                if sl.count('м') == 2 and sl.count('и') == 3 and sl.count('к') == 1 and sl.count('р') == 1 and sl.count('я') == 1:
                                    mass2.append(sl)



print(len(set(mass2)))

# 3360
