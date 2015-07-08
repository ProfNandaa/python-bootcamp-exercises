import unittest, factorial

class FactorialTest(unittest.TestCase):
	def testPositiveFactorial(self):
		self.assertEqual(factorial.factorial(5), 120, msg="5 factorial should return 120")
		self.assertEqual(factorial.factorial(4), 24, msg="4 factorial should return 24")
	
	def testNegativeFactorial(self):
		self.assertEqual(factorial.factorial(-9), -1, msg="Factorial of a negative number should return false")

	def testAlphaticalInput(self):
		self.assertEqual(factorial.factorial('ieiee'), -1,  msg="Factorial should return false for alphatical input")

	def testDecimalInput(self):
		self.assertEqual(factorial.factorial(2.3453), -1,  msg="Factorial should return false for a decimal number")

if __name__ == '__main__':
	unittest.main()
