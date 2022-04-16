# считать число 
# сделать все двузначные числа на отрезке заданосм в условии 
# перебрать двумы форами и посчитать разницу если она подходит то +1  
kol = 0

for n in range(100, 1000):
    a = int(str(n)[0] + str(n)[1])
    b = int(str(n)[0] + str(n)[2])
    c = int(str(n)[1] + str(n)[0])
    d = int(str(n)[1] + str(n)[2])
    e = int(str(n)[2] + str(n)[0])
    f = int(str(n)[2] + str(n)[1])
    mass = list(filter(lambda x: len(str(x)) == 2, [a,b,c,d,e,f]))
    if len(mass) >= 2:
        mini = min(mass)
        maxi = max(mass)
        
        if (maxi - mini) == 58:
            kol += 1
        
print(kol)
