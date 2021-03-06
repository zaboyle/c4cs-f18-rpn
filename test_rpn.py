import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate('4 3 -')
        self.assertEqual(1, result)
    
    def test_divide(self):
        result = rpn.calculate('6 3 /')
        self.assertEqual(2, result)
    
    def test_multi(self):
        result = rpn.calculate('4 5 *')
        self.assertEqual(20, result)

    def test_exponent(self):
        result = rpn.calculate('2 4 ^')
        self.assertEqual(16, result)
    
    def test_toomany(self):
        with self.assertRaises(ValueError):
            result = rpn.calculate('1 2 3 +')

if __name__ == '__main__':
    unittest.main()


