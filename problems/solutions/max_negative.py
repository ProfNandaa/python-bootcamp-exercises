def max_negative(a):
	maxn = None
	
	for i in a:
		if i < 0:
			maxn = i
			if i > maxn:
				maxn = i

	return maxn