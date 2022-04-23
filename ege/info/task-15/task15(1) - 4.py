'''
равносильно : ==
следование : <=
стрелочка вверх : and 
стрелочка вниз : or
'''

def check(x, a):
    return ((a % 9) == 0) and ((280 % x) == 0) <= (((a % x) != 0) <= ((730 % x) != 0))

k = 0 

for i in range(1, 1001):
    if all(check(x, i) == True for x in range(1, 100001)):
        k += 1

print(k) 
        

# 11
