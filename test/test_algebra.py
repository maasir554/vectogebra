"""
---------------------------------------------------------------------
vectogebra/test/test_algebra.py
---------------------------------------------------------------------
File under project "vectogebra"
---------------------------------------------------------------------
This file contains the test cases for the attributes of vector class.
---------------------------------------------------------------------
License: MIT License (see LICENSE in project's main directory)
copyright: (C) 2022 Mohammad Maasir
---------------------------------------------------------------------
- date created: 9th of May, 2022 (11:35 PM)
- last modified: 9th of May, 2022
---------------------------------------------------------------------
contributor(s): Mohammad Maasir
---------------------------------------------------------------------
github: github.com/maasir554/vectogebra/vectogrbra/vector.py
---------------------------------------------------------------------
report an issue at: github.com/maasir554/vectogebra/issues
---------------------------------------------------------------------
email: maasir554@gmail.com


"""

# NOTE: do NOT run this file directly.

# Instead, open console or terminal and change dirctory to root directory of this project : 
# $ cd vectogebra
# then, run the following command:
# python -m unittest test/test_algebra.py 
# OR
# python -m unittest test.test_algebra
# OR 
# python -m unittest discover 

## and you should see an OK message.
## if not, then you have some test case(s) that failed.

#####################################################################

############## the following block is VERY important ################

#####################################################################
#------------------------------------------------------(result of a lot of research, trial and error)
import pathlib
import sys
currentDIR = pathlib.Path(__file__).resolve().parent
rootDIR = currentDIR.parent
vectogebraMAIN = rootDIR / 'src' /'vectogebra'
sys.path.append(str(vectogebraMAIN))
sys.path.append(str(rootDIR))
# os module can also be used here. but pathlib is easier to work with
#------------------------------------------------------  (added the src/vectogevra to the path for the test file to work)
import unittest

# from vector import vector as vect

from src.vectogebra.vector import vector as vect
# if you wish to run directly, you can use the following:(disable the above line first)
# from vector import vector as vect
v1 = vect(1,2,3)
v2 = vect(4,5,6)
v3 = vect(2,2,2)


class TestStringMethods(unittest.TestCase):
    
    # ########################################## #

    # ######### ALGEBRIC OPERATORS ############# #

    # ########################################## #

    def test_addition_operator(self):
        self.assertEqual(v1+v2, vect(5,7,9))
        self.assertEqual(v1+v2+v3, vect(7,9,11))

    def test_subctraction_operator(self):
        self.assertEqual(v1-v2, vect(-3,-3,-3))
        self.assertEqual(v1-v2-v3, vect(-5,-5,-5))

    def test_dot_operator(self):
        self.assertEqual(v1*v2, 32)
        self.assertEqual(v1*v2*v3, 32*v3)

    def test_cross_operator(self):
        self.assertEqual(v1^v2, vect(-3,6,-3))
        self.assertEqual(v1^v2^v3, vect(18,0,-18))  #same as v1^(v2^v3)
    
    def test_scalar_multiplication(self):
        self.assertEqual(v1*2, vect(2,4,6))
        self.assertEqual(2*v1, vect(2,4,6))

    def test_scalar_division(self):
        self.assertEqual(v1/2, vect(0.5,1,1.5))

    def test_unary_operators(self):
        self.assertEqual(-v1, vect(-1,-2,-3))
        self.assertEqual(-v2,vect(-4,-5,-6))
        self.assertEqual(-v3,vect(-2,-2,-2))
        #for + uunary operator
        self.assertEqual(+v1, vect(1,2,3))
        self.assertEqual(+v2,vect(4,5,6))
        self.assertEqual(+vect(-1,5,-56),vect(-1,5,-56))
    
    def test_round_function(self):
        a = vect(1.29,2.36,3.45)
        b = vect(1.0453,2.0453,3.0453)
        self.assertEqual(round(a), vect(1,2,3))
        self.assertEqual(round(b), vect(1,2,3))
        self.assertEqual(round(a,1), vect(1.3,2.4,3.5))



if __name__ == '__main__':
    unittest.main()
