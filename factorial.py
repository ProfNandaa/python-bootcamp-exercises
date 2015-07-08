def factorial(n):
	if type(n) == float:
		return -1
	if type(n) != int:
		return -1
	if n < 0:
		return -1
	
	result = 1
	
	while n > 0:
		result = result * n
		n = n - 1
	
	return result