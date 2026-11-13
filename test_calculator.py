
#Github link: https://github.com/sunandrew057/lab11-HO-AS/tree/main
#Partner 2: Hope Ong
#Partner 1: Andrew Sun

import unittest
import math
from calculator import (add, subtract, multiply, div, logarithm, square_root,hypotenuse)

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
         #return unittest.TestCase.add(self)
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self): # 3 assertions
        #return unittest.TestCase.sub(self)
        self.assertEqual(subtract(10, 4), 6)

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


# Do not touch this
if __name__ == "__main__":
    unittest.main()