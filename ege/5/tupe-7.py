param = 100
rez = 9
mini = False

if mini:
    for i in range(param + 1):
        if int(str(bin(i)[2:])[::-1], 2) == rez:
            print(i)
            break
else:
    for  i in range(param, 0, -1):
        if int(str(bin(i)[2:])[::-1],2) == rez:
            print(i)
            break
    
