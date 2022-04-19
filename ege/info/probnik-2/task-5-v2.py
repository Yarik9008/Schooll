

for number in range(15,10000000):
    a = list(str(number))
    data = list(zip(a[:-1], a[1:]))
    data = [int(i[0] + i[1]) for i in data]
    out = min(data) + max(data)
    if out == 153:
        print(number)
        break