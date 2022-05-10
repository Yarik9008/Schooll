num = (65**25 + 4**10) - (16**20 + 32 ** 3)

def convert(num, baze):
    new = ''
    while num > 0:
        new = (str(num % baze)) + new
        num //= baze
    return new

print(convert(num,4).index('2') + 1)

# 4