def f(x, comm):
    if x > 11:
        return 0
    elif x == 11:
        return 1
    if comm == 'um':
        return f(x + 1, 'pl') + f(x + 2, 'pl')
    else:
        return f(x + 1, 'pl') + f(x + 2, 'pl') + f(x * 2, 'um')



print(f(1))