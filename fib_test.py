import unittest
import fibonacci as fib

class FibTest(unittest.TestCase):
	def test_series(self):
		self.assertEqual(fib.fib_series(4),[0,1,1,2],msg="fib_series(4) \
			should be equal to [0,1,1,2]")
		self.assertEqual(fib.fib_series(2),[0,1],msg="fib_series(2) \
			should be equal to [0,1]")

	def test_sum_series(self):
		self.assertEqual(fib.fib_series_sum(2),1,msg="fib_series_sum(2) \
			 should be 	equal to 1")
		self.assertEqual(fib.fib_series_sum(10),30,msg="fib_series_sum(2) \
			 should be 	equal to 1")

if __name__ == '__main__':
	unittest.main()