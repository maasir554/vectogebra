from re import S
import unittest
import math

#---------------------------------------------------------
import pathlib
import sys
currentDIR = pathlib.Path(__file__).resolve().parent
rootDIR = currentDIR.parent
vectogebraMAIN = rootDIR / 'src' /'vectogebra'
sys.path.append(str(vectogebraMAIN))
sys.path.append(str(rootDIR))
#----------------------------------------------------------

from src.vectogebra.vector import vector as vect

from src.vectogebra import utilities as vut

from src.vectogebra import geometry as geo

a = vect(1,3,5)
b = vect(3,5,7)
c = vect(0,4)
d = vect(3,0)

class TestStringMethods(unittest.TestCase):
    def test_section(self):
        self.assertEqual(geo.divider(a,b,1,1), vect(2,4,6))

    def test_distance(self):
        self.assertEqual(geo.distance(c,d), 5.0)     


if __name__ == '__main__':
    unittest.main()