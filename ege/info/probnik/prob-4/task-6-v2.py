kol = 0

for number in range(1000000):
    s = number
    s = s // 7 
    n = 1 

    while s < 255:
        s = s + n 
        n = n + 1 

    if n == 8:
        kol += 1
        

print(kol)