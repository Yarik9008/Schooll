kol = 0 

def megafun(n):
    if n % 2  == 0 and n >= 0:
        return n / 2
    else:
        return 1 + megafun(n - 1)

for i in range(1,501):
    if megafun(i) == 8:
        print(i)
        kol += 1

print(kol)

