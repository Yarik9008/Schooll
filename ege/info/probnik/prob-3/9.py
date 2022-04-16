from ctypes.wintypes import PPOINT
from pprint import pprint


path1 = 'ege\probnik\prob-3\data\9.txt'

mass = open(path1, 'r').readlines()
mass = [i[:-2].split('\t') for i in mass]
mass = list(map(lambda x: [int(i) for i in x], mass))


