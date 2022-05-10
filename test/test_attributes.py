"""
---------------------------------------------------------------------
vectogebra/test/test_attributes.py
---------------------------------------------------------------------
File under project "vectogebra"
---------------------------------------------------------------------
This file contains the test cases for the attributes of vector class.
---------------------------------------------------------------------
License: MIT License (see LICENSE in project's main directory)
copyright: (C) 2022 Mohammad Maasir
---------------------------------------------------------------------
- date created: 9th of May, 2022 (09:55 PM)
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
# python -m unittest test/test_attributes.py 
# OR
# python -m unittest test.test_attributes
# OR 
# python -m unittest discover 

## and you should see an OK message.
## if not, then you have some test case(s) that failed.

#------------------------------------------------------
import pathlib
import sys
currentDIR = pathlib.Path(__file__).resolve().parent
rootDIR = currentDIR.parent
vectogebraMAIN = rootDIR / 'src' /'vectogebra'
sys.path.append(str(vectogebraMAIN))
sys.path.append(str(rootDIR))
#------------------------------------------------------

import unittest

from src.vectogebra.vector import vector as vect
#from vector import vector as vect 
#do NOT delete the above comment.

v1 = vect(1,2,3)
v2 = vect(4,5,6)
v3 = vect(2,2,2)

class TestStringMethods(unittest.TestCase):

    ############################################
    ######## VECTOR CLASS ATTRIBUTES ###########
    ############################################

    def test_vector_components(self):
        self.assertEqual(v1.i, 1)
        self.assertEqual(v1.j, 2)
        self.assertEqual(v1.k, 3)
    

    def test_magnitude(self):
        self.assertEqual(v1.magnitude, 3.7416573867739413)
    
    def test_magnitude_squared(self):
        self.assertEqual(v1.magnitude_squared,14)

    def test_unit_vector(self):
        self.assertEqual(v1.unit_vector, vect(0.2672612419124244,0.5345224838248488,0.8017837257372732))
    
    
    


    # def test_subctraction(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
