# +1 *2


'''
report
19- 
20- 
21- 
'''

from functools import lru_cache

def move(h):
    a,b = h
    return(a+1, b), (a, b+1), (a*2, b), (a, b*2)

def game(h):
    if sum(h) >= 30:
        return 'w'
    
    if any(game(n) == 'w' for n in move(h)):
        return 'p1'

    if any(game(n) == 'p1' for n in move(h)):
        return 'b1'
    
for q in range(1,30):
    for w in range(1,30):
        rez