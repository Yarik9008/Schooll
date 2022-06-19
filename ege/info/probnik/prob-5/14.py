num = 7 * 729**543 - 6*81**765 - 5*9**987 - 20

def convert(num):
    new = ''
    while num > 0:
        new = str(num % 9) + new
        num //= 9
    return new

print(convert(num).count('8'))
print(convert(num))