import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(-3 * 3), -9)
        self.assertEqual(mul(0 * 5), 0)
        self.assertEqual(mul(5 * 2), 10)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(5, 2), 0.4)
        self.assertAlmostEqual(div(4, 2), 0.5)
        self.assertAlmostEqual(div(-3, 6), -2)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(5, 2), 5.3851648)
        self.assertAlmostEqual(hypotenuse(0, 3), 3)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(6), 2.4494897)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()