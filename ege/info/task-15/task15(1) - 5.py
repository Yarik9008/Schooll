'''
равносильно : ==
следование : <=
стрелочка вверх : and 
стрелочка вниз : or
'''

def check(x, a):
    return (((x % 84) != 0) or (x % 90) != 0) <= ((x % a) != 0)

k = 0 

for i in range(1, 1000001):
    if all(check(x, i) == True for x in range(1, 100001)):
        print(i)

 
# 1260
