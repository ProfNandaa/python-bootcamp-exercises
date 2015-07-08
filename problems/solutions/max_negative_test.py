import unittest
import max_negative as mn

class MaxNegTest(unittest.TestCase):
	def test_all_negative(self):
		self.assertEqual(mn.max_negative([-20,-10,5,-50,-3]),-3, msg="\
			should return -3")

	def test_mixture(self):
		self.assertEqual(mn.max_negative([-20,5,10,-2,-1,10,0]),-1, msg="\
			should return -1")

	def test_all_positive(self):
		self.assertEqual(mn.max_negative([20,10,10,5,2,1,10]),None, msg="\
			should return -1")

if __name__ == "__main__":
	unittest.main()

