for i in range(10000000000):
    mass = list(str(i))
    mass1 = sum([int(a) for a in mass[::2]])
    mass2 = sum([int(a) for a in  mass[1::2]])
    if mass1-mass2 == 26:
        print(i)
        break

    
# 1070909