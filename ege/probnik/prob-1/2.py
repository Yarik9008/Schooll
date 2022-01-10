for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((x == (not y)) <= ((x and w) == (z and (not w)))) == 0:
                    print(x,y,z,w)

# W Z Y X 
