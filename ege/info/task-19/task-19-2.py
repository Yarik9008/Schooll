from functools import lru_cache
import re

# 19 - 24
# 20 - 8 22 23 
# 21 - 21
# +1 + 2 *3

def move(h):
    return h + 1, h + 2, h*3 

@lru_cache(None)
def game(h):
    if h >= 74:
        return 'w'

    if any(game(n) == 'w' for n in move(h)):
        return 'p1'
    
    if all(game(n) == 'p1' for n in move(h)):
        return 'v1'

    if any(game(n) == 'v1' for n in move(h)):
        return 'p2'

    if all(game(n) == 'p2' or game(n) == 'p1' for n in move(h)):
        return 'v2'

for i in range(1,74):
    rez = game(i) 
    if rez == 'v2':
        print(i,rez)
        
