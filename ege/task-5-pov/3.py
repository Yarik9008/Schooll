kol = 0

for i in range(1,1000000):
    if i % 3 ==0:
        num = i /  3
    else:
        num = i -  1 
    if num % 5 == 0:
        num  /= 5 
    else:
        num -= 1
    if num % 11 == 0:
        num  /= 11 
    else:
        num -= 1

    if num == 6:
        kol += 1 

print(kol)
    
# 6