'''
равносильно : ==
следование : <=
стрелочка вверх : and 
стрелочка вниз : or
'''

def check(x, y, a):
    return (75 != (2 * x + 3 * y)) or (a > 3 * x) or (a > 2 * y)

k = 0 

for i in range(1, 1001):
    if all(check(x, y, i) == True for x in range(1, 1001) for y in range(1, 1001)):
        print(i)
        break
        

# 35 