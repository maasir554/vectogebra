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
o = vect(0,0)

class TestStringMethods(unittest.TestCase):
    def test_section(self):
        self.assertEqual(geo.divider(a,b,1,1), vect(2,4,6))

    def test_distance(self):
        self.assertEqual(geo.distance(c,d), 5.0) 

    def test_area_triangle(self):
        a = vect(0,2)
        b = vect(2,0)
        c = vect(0,0)
        self.assertEqual(geo.area_triangle(a,b,c), 2.0) 
        self.assertEqual(geo.area_triangle(c,b,a), 2.0)
        self.assertEqual(geo.area_triangle(b,c,a), 2.0)
        self.assertEqual(geo.area_triangle(a,c,b), 2.0)


    def test_area_line(self):
        self.assertEqual(geo.area_line(c,d), 6)
        self.assertEqual(geo.area_line(d,c), -6)

    def test_area_polygon(self):
        self.assertEqual(geo.area_polygon(*[o,c,d]),6)
        self.assertEqual(geo.area_polygon(o,c,d),6)


if __name__ == '__main__':
    unittest.main()
