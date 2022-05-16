from itertools import combinations_with_replacement

data = list(combinations_with_replacement('ЛЕОНИД' , 6))
print(len(data))
data = list(filter(lambda x: x.count('Л') == 2 and x.count('О') >= 1, data))
print(len(data))