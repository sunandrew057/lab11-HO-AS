
#Github link: https://github.com/sunandrew057/lab11-HO-AS/tree/main
#Partner 2: Hope
#Partner 1: Andrew

import unittest
from calculator import *\

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
         return unittest.TestCase.add(self)

    def test_subtract(self): # 3 assertions
         return unittest.TestCase.sub(self)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     call division function inside, example:
         with self.assertRaises(ZeroDivisionError):
              div(0, 5)
    #     fill in code


            unittest.TestCase.div(self)

    def test_logarithm(self): # 3 assertions
         return unittest.TestCase.log(self)

    def test_log_invalid_base(self): # 1 assertion
    #     use same technique from test_divide_by_zero
        #     fill in code
        with self.assertRaises(ValueError):
            div(0, 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()