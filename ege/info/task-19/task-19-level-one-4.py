'''
report
19- 12
20- 2123
21- 20
'''

from functools import lru_cache

def move(h):
    a,b = h
    return (a +1, b),(a, b +1), (a *2, b), (a,b*2)

@lru_cache(None)
def game(h):
    if sum(h) >= 53:
        return 'w'
    
    if any(game(i) == 'w' for i in move(h)):
        return 'p1'

    if all(game(i) == 'p1' for i in move(h)):
        return 'v1'

    if any(game(i) == 'v1' for i in move(h)):
        return 'p2'
    
    if all(game(i) == 'p1' or game(i) == 'p2'  for i in move(h)):
        return 'v2'

for a in range(1, 47):
    rez = game((5, a))
    if rez != None:
        print(a, rez)

