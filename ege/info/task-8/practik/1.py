mass = sorted(list('солнце'))
kol = 0
for a1 in mass:
    for a2 in mass:
        for a3 in mass:
            for a4 in mass:
                for a5 in mass:
                    for a6 in mass:
                        sl = a1+a2+a3+a4+a5+a6
                        if sl.count('о') <= 2 and sl.count('ц') == 1:
                            kol += 1

print(kol)

