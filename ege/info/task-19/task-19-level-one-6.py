#  +3 *2

'''
report
19- 18
20- 17
21- 2627
'''

from functools import lru_cache


def move(h):
    a,b = h
    return (a+3,b), (b+3, a), (a*2,b), (b*2, a)

@lru_cache(None)
def game(h):
    if sum(h) >= 79:
        return 'w'
    
    if any(game(n) == 'w' for n in move(h)):
        return 'p1'
    
    if all(game(n) == 'p1' for n in move(h)):
        return 'b1'

    if any(game(n) == 'b1' for n in move(h)):
        return 'p2'

    if all(game(n) == 'p1' or game(n) == 'p2' for n in move(h)):
        return 'b2'

for i in range(1,70):
    rez = game((9,i))
    if rez == 'b2':
        print(rez, i)

