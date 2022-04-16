from random import randint
mass = [randint(1,10000) for i in range(30)] # формирование массива 

print(f'data: {mass}') # исходные элименты

masssort = sorted(mass[::1]) # сортировка по возрастанию 

print(f'min: {masssort[0] + masssort[1]}') #  минимальная сумма
print(f'index: {mass.index(masssort[0])}, {mass.index(masssort[1])}') # индексы 

# 
