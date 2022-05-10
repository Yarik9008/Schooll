#  +2 *2

'''
report
19- 19
20- 18
21- 2933
'''

from functools import lru_cache


def move(h):
    a, b = h
    return (a*2, b), (a, b*2), (a+2, b), (a, b+2)
@lru_cache(None)
def game(h):
    if sum(h) >= 82:
        return 'w'
    
    if any(game(n) == 'w' for n in move(h)):
        return 'p1'

    if all(game(n) == 'p1' for n in move(h)):
        return 'b1'

    if any(game(n) == 'b1' for n in move(h)):
        return 'p2'

    if all(game(n) == 'p2' or game(n) == 'p1' for n in move(h)):
        return 'b2'


for i in range(1,72):
    rez  = game((9, i))
    if rez == 'b2':
        print(rez, i)