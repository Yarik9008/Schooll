mass = list('росомаха')
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
                                if sl.count('р') == 1 and sl.count('о') == 2 and sl.count('с') == 1 and sl.count('м') == 1 and sl.count('а') == 2 and sl.count('х') == 1:
                                    if 'оа' not in sl and 'ао' not in sl and 'рс' not in sl and 'ср' not in sl and 'см' not in sl and 'мс' not in sl and 'хр' not in sl and 'рх' not in sl and 'рм' not in sl and 'мр' not in sl and 'мх' not in sl and 'хм' not in sl:
                                        mass2.append(sl)



print(len(set(mass2)))