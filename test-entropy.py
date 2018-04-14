import unittest
import numpy as np
import entropy

# def entropy(ps):
#     items = ps * np.log(ps)
#     return -np.sum(items)

class TestEntropy(unittest.TestCase):
	
	def test_equal_probability(self):
		def test(count):
			self.assertTrue(np.isclose(entropy([1./count for k in range(count)]), np.log(count)))
		test(2)
		test(20)
		test(200)

	def test_invalid_probability(self):
		with self.assertRaises(ValueError):
			entropy([0.1, 0.5])


if __name__ == '__main__':
	unittest.main()