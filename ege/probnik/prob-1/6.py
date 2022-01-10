kol = 0
for i in range(999999):
    s = i
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s += 13
        n *= 2
    if n == 128:
        kol += 1
print(kol)

# 40

