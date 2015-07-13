import sys

argv = sys.argv[1:]

def bsearch(A,n):
	last = len(A) - 1
	first = 0

	count = 0

	while first <= last:
		count += 1
		if argv and argv[0] == "-v":
			print "Count ",count

		m = (last + first)//2
		if A[last] == n:
			return last
		elif A[first] == n:
			return first
		elif A[m] == n:
			return m
		else:
			if A[m] > n:
				last = m - 1
			else:
				first = m + 1



a = [20,50,60,100,150,200,210,250]

print bsearch(a,20)