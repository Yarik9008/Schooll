from functools import lru_cache

# +1 *2
# 19 - 18
# 20 - 31 34 
# 21 - 30

def move(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(None)
def game(h):
    if sum(h) >= 77:
        return 'w'
    
    if any(game(n) == 'w' for n in move(h)):
        return('p1')
    
    if all(game(n) == 'p1' for n in move(h)):
        return('v1')

    if any(game(n) == 'v1' for n in move(h)):
        return('p2')

    if all(game(n) == 'p2' or game(n) == 'p1' for n in move(h)):
        return('v2')

for i in range(1,69):
    rez = game((7,i))
    if rez == 'p2':
        print(i, rez)
        