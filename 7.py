mass = []
for i in range(12345, 1234567):
    if len(set(list(str(i)))) == 1:
        mass.append(i)

print(len(mass))
print(mass[-1])