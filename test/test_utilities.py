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


#from vector import vector as vect
#import utilities as vut
""" 
    enable the above lines and comment two 
    the lines below
    to run this file directly.
"""

import math

from src.vectogebra.vector import vector as vect

from src.vectogebra import utilities as vut

v1 = vect(1,2,3)
v2 = vect(4,5,6)
v3 = vect(2,2,2)
v4= vect(20,20,20)

class TestStringMethods(unittest.TestCase):
    
    ############################################

    #### UTILITY FUNCTIONS FOR CLASS VECTOR ####

    ############################################

    def test_add_function(self):
        self.assertEqual(vut.add(v1,v2), vect(5,7,9))
        self.assertEqual(vut.add(v1,v2,v3), vect(7,9,11)) # Any number of vectors can be added.
    
    def test_angle_function(self):
        self.assertEqual(vut.angle(v1,v2), 0.2257261285527342)
        self.assertEqual(vut.angle(v3,v4), 0)
        self.assertEqual(vut.angle(vect(1,0,0),vect(0,1,0)), math.pi/2)



if __name__ == '__main__':
    unittest.main()