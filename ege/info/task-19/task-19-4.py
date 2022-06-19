from functools import lru_cache

# + 1 * 2


def move(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)

@lru_cache(None)
def game(h):
    if sum(h) >= 63:
        return 'w'
    
    if any(game(n) == 'w' for n in move(h)):
        return 'p1'

    if all(game(n) == 'p1' for n in move(h)):
        return 'v1'

    if any(game(n) == 'v1' for n in move(h)):
        return 'p2'

    if all(game(n) == 'p2' or game(n) == 'p1' for n in move(h)):
        return 'v2'


for i in range(1,63):
    rez = game((5,i))
    if rez == 'v2':
        print(rez, i)

    

# 15
# 26 28 
# 25 