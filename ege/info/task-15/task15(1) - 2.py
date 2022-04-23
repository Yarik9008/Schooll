'''
равносильно : ==
следование : <=
стрелочка вверх : and 
стрелочка вниз : or
'''

def check(x, a):
    return (a % 5 == 0) and ( (not( 2020 % a == 0)) <= ((x % 1718 == 0) <= (2023 % a == 0)))


for i in range(1, 10000):
    if all(check(x, i) == True for x in range(1, 100001)):
        print(i) 

# 6
