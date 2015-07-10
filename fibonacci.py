def fib_series(n):
	series = []

	for i in range(0,n):
		if i <= 1:
			series.append(i)
		else:
			num = series[len(series)-1] + series[len(series)-2];
			series.append(num)

	return series;

def fib_series_sum(n,num_type=None):
	total = 0
	if num_type is "even":
		for i in fib_series(n):
			if i % 2 == 0:
				total += i
	elif num_type is "odd":
		for i in fib_series(n):
			if i % 2 == 1:
				total += 1
	else:
		return sum(fib_series(n))
