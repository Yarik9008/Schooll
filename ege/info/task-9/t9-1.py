from pprint import pprint
tab = open('ege/task-9/9-127.csv', 'r')
tab = [[int(a) for a in i.split(';')] for i in tab.readlines()]
pprint(tab)
