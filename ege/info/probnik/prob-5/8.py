mass = sorted(list('пятьдней'))
num = 1
for q in mass:
    for w in mass:
        for e in mass:
            for r in mass:
                if len(set([q,w,e,r])) == 4 and 'я' not in q+w+e+r and 'e' not in q+w+e+r:
                    print(num)
                num += 1

#3428 