kol = 0

for i in range(20000000):
    num1 = str(bin(i)[2:])
    if len(num1) >= 2:
        num1 += num1[-2] + num1[1]
        num2 = int(num1, 2)
        if num2 >= 150 and num2 <= 200:
            kol += 1

print(kol)