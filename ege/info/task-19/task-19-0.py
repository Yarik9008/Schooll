# +2 * 2
from functools import lru_cache

def move(h):
    a,b = h
    return (a +2 ,b), (a,b +2), (a*2,b), (a,b*2)

@lru_cache(None)
def game(h):
    if sum(h) >= 231:
        return 'w'
    
    if any(game(n) == 'w' for n in move(h)):
        return 'p1'

    if all(game(i) == 'p1' for i in move(h)):
        return 'v1'
    
    if any(game(i) == 'v1'  for i in move(h)):
        return 'p2'

for i in range(1,213):
    rez = (game((17, i)))
    if rez == 'p2':
        print(i, rez)


98
104
105
