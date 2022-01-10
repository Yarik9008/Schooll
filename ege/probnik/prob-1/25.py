def m(n):
    kol = []
    for i in range(2,n):
        if len(kol) < 5:
            if n % i == 0:
                kol.append(i)
    else:
        a = 1
        for i in kol:
            a *= i
        return a 

mass = []
for i in range(20000000000):
    if len(mass) < 5:
        a = m(i)
        if a > 0 and a < i:
            print(a)
            mass.append(a)
    else:
        break
    
print(mass)

