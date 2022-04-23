'''
равносильно : ==
следование : <=

'''

def check(x, a):
    return (not((x % 16 == 0) == (x % 24 == 0))) <= (x % a == 0)


for x in range(1, 1000):
    if all(check(i, x) == True for i in range(1, 1001)):
        print(x) 

# 8н