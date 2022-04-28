'''
report 
19 - 4
20 - 314
21 - 13

'''

from functools import lru_cache


def move(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 3, b), (a, b * 3)

@lru_cache(None)
def game(h):
    if sum(h) >= 49:
        return 'w'
    
    if any(game(m) == 'w' for m in move(h)):
        return 'p1'
    
    if all(game(m) == 'p1' for m in move(h)):
        return 'v1'

    if any(game(m) == 'v1' for m in move(h)):
        return 'p2'
    
    if all(game(m) == 'p1' or game(m) == 'p2' for m in move(h)):
        return 'v2'
    

    
for i in range(1, 43):
    rez = game((5,i))
    if rez != None:
        print(i, rez)