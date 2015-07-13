class BinarySearch(list):
	def __init__(self,a,b):
		data = range(0,a,b)
		super(type(self),self).__init__(data)
		self.length = a

	def search(self,n):
		A = self

		last = len(A) - 1
		first = 0

		count = 0

		while first <= last:
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



a = BinarySearch(10,2)

print a.search(2)
print a[2]