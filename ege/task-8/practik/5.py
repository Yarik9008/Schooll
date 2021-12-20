mass = list('банкир')
kol = 0
for a1 in mass:
    for a2 in mass:
        for a3 in mass:
            for a4 in mass:
                for a5 in mass:
                    for a6 in mass:
                        sl  = a1 + a2 + a3 + a4 + a5 + a6
                        if  sl.count('а') <= 1 and  sl.count('и') <= 1:
                            kol += 1

print(kol)

# 720 

