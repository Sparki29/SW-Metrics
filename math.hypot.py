import math 
import unittest

def hypotenuse(side1_, side2_):
	return math.sqrt(side1_**2 + side2_**2)


class Function(unittest.TestCase):
		
	def test_equal(self):
		self.assertEqual(hypotenuse(5, 5), 7.0710678118654755)
	
	def test_incorrect_(self):
		with self.assertRaises(TypeError):
			hypotenuse('a', 'a')
		
	def test_noarg(self):
		with self.assertRaises(TypeError):
			hypotenuse()

if __name__ == '__main__':
    unittest.main()

