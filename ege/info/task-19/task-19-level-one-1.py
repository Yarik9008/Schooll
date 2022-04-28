# штука для буферизации 
from functools import lru_cache

'''
report

19) 18
20) 3134
21) 30 

'''


# обозначает возможные хода 
def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)


# описание игры 
@lru_cache(None)
def game(h):
    # проверка на то что данная позиция является выйграшной 
    if sum(h) >= 77:
        return 'w'
    # проверка что есть хотя бы один ход в выгрушную позицию среди доступных ходов 
    if any(game(m) == 'w' for m in moves(h)):
        return 'P1'

    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'

    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'

    if all(game(m) == 'P2' or  game(m) == 'P1' for m in moves(h)):
        return 'B2'

for s in range(1,70):
    # 10 камней начаьное количиство 
    if game((7,s)) != None :
        # вывод всех выграшных позиций 
        print(s, game((7, s)))

