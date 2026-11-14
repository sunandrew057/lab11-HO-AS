#Github link: https://github.com/sunandrew057/lab11-HO-AS/tree/main
#Partner 2: Hope Ong
#Partner 1: Andrew Sun

import unittest
import math
from calculator import (add, subtract, mul, div, logarithm, square_root,hypotenuse)

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
         #return unittest.TestCase.add(self)
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self): # 3 assertions
        #return unittest.TestCase.sub(self)
        self.assertEqual(subtract(10, 4), 6)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(-3, 3), -9)
        self.assertEqual(mul(0, 5), 0)
        self.assertEqual(mul(5, 2), 10)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(5, 2), 0.4)
        self.assertAlmostEqual(div(4, 2), 0.5)
        self.assertAlmostEqual(div(-3, 6), -2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     call division function inside, example:
         with self.assertRaises(ZeroDivisionError):
              div(0, 10)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)

    def test_log_invalid_base(self): # 1 assertion
    #     use same technique from test_divide_by_zero
        #     fill in code
        with self.assertRaises(ValueError):
            logarithm(1, 8)

    # def test_log_invalid_base(self): # 1 assertion
    #     use same technique from test_divide_by_zero
        #     fill in code
        with self.assertRaises(ValueError):
            logarithm(1, 8)
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
