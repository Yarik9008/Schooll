
finish = 63
init_number = 7
error_number = 43


def f(n):
	if n == 63:
		return 1
	if n > finish or n == err:
		return 0
	return f(n + 2) + f(2 * n - 1) + f(2 * n + 1)
	
	
print(f(init_number))