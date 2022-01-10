for s in range(100000000000):
    mass = [int(i) for i in list(str(s))]
    otvsum = sum(list(filter(lambda x: x % 2 == 0, mass)))
    mass2 = [int(i) for i in list(str(s))]
    ch = True
    mass3 = []
    for i in mass2:
        if ch:
            ch = False
        else:
            ch = True
            mass3.append(i)
    sumch = sum(mass3)
    if otvsum - sumch == 13:
        print(s)
        break
 
 # 618
 