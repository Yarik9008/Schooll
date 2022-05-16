num = 934
number = str(bin(num))[2:]
if number.count('1') % 2 == 0:
    number = '1' + number + '00'
else:
    number 