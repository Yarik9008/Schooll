from tkinter import N


for s in range(-14, -1000, -1):
    i = s
    s = (s + 13) * 10
    n = 512
    while s < 0:
        n = n // 2
        s = s + n
    if n == 8:
        print(i)
        