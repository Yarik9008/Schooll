
for i in range(100, 10000):
    num = str(bin(i))[2:]
    for a in range(2):
        if num.count('1') > num.count('0'):
            num += '0'
        elif num.count('0') > num.count('1'):
            num += '1'
        elif num.count('1') == num.count('0'):
            num += num[-1]
    if int(num, 2) % 4 == 0 and int(num, 2) % 8 != 0:
        print(i)
        break

# 101