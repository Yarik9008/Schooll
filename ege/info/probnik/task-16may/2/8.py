from msilib.schema import MsiAssembly


mass = sorted(list('ужемай'))
kol = 0
kol_all = 0
for q in mass:
    for w in mass:
        for e in mass:
            for r in mass:
                for t in mass:
                    kol_all += 1
                    if not w == r:
                        kol += 1 

print(kol)
print(kol_all)
                        
# 6480
