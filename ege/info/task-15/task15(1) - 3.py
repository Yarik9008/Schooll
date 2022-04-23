'''
равносильно : ==
следование : <=
стрелочка вверх : and 
стрелочка вниз : or
'''

def check(x, a):
    return ((x & 13) == 0) <= (((x & 40) != 0) <= ((x & a) != 0))
for i in range(1, 10000):
    if all(check(x, i) == True for x in range(1, 100001)):
        print(i) 
        

# 6
