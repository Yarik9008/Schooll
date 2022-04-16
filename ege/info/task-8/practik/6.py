mass = sorted(list('азнс'), reverse=False)
kol = 0
ch = False
for a1 in mass:
    for a2 in mass:
        for a3 in mass:
            for a4 in mass:
                for a5 in mass:
                    sl = a1+a2+a3+a4+a5
                    if sl == 'сазан':
                        ch = True
                    if sl == 'занас':
                        ch = False
                    if ch:
                        kol += 1

print(kol)

# 238
