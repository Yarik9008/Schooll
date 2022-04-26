'''
равносильно : ==
следование : <=
стрелочка вверх : and 
стрелочка вниз : or
'''

def check(x, a):
    return ((x % 6 == 0) <= (x % 14 != 0)) or ((x + a >= 70) and ((a % 20 == 0)))
    
for i in range(1, 10000):
    if all(check(x, i) == True for x in range(1, 100001)):
        print(i) 
        
