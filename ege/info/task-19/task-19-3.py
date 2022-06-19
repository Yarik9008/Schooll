from functools import lru_cache

def move(h):
    a,b = h
    return (a+3,b), (a,b+3), (a*2,b), (a,b*2)

@lru_cache(None)
def game(h):
    if h[0] >= 21 or h[1] >= 21:
        return 'w'
    
    if any(game(n) == 'w' for n in move(h)):
        return 'p1'
    
    if all(game(n) == 'p1' for n in move(h)):
        return 'v1'

    if any(game(n) == 'v1' for n in move(h)):
        return 'p2'

    if all(game(n) == 'p2' for n in move(h)):
        return 'v2'

    if any(game(n) == 'v2' for n in move(h)):
        return 'p3'

    if all(game(n) == 'p3' for n in move(h)):
        return 'v3'



for i in range(1,21):
    rez = game((4,i))
    if rez == 'v2' or rez == 'v3':
        print(rez, i)

print(game((4,4)))






# 19 2 4 
# 20 2 
# 21 14567