import unittest


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
    def test_divider(self):
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

    def test_coplanar(self):
        v1 = vect(1,1)
        v2 = vect(1,2)
        v3 = vect(2,1)
        #---
        a1 = vect(1,1,1)
        a2 = vect(1,2,1)
        a3 = vect(2,1,1)
        #---
        b1 = vect(789,0.0051,5656.89)
        b2 = vect(59851,7006989,589656.89)
        #---
        self.assertTrue(geo.coplanar(v1,v2,v3))
        self.assertTrue(geo.coplanar(a1,a2,a3))
        self.assertFalse(geo.coplanar(b1,a1,b2,a3))
        self.assertTrue(geo.coplanar(a1,a1,a2,a2))

if __name__ == '__main__':
    unittest.main()
