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

    def test_class_line(self):
        a1 = vect('2 1 -2')
        b1 = vect('6 -8 10')
        a2 = vect('-1 -1 5')
        b2 = vect('6 7 -2')
        l1 = geo.line(p=a1,d=b1)
        l2 = geo.line(p=a2,d=b2)
        #---
        self.assertEqual(l1.point, a1)
        self.assertEqual(l1.direction, b1)
        self.assertEqual(l2.point, a2)
        self.assertEqual(l2.direction, b2)
        #---
        self.assertFalse(l1.intersects(l2))
        self.assertFalse(l2.intersects(l1))
        #---
        self.assertEqual(l1.distance(l2),5.091168824543141)
        self.assertEqual(l2.distance(l1),5.091168824543141)
        self.assertEqual(l1.intersection(l2),None)
        self.assertEqual(l2.intersection(l1),None)
        #---

        line1 = geo.line(p = vect(0,0,0), d = vect(1,1,1))
        line2 = geo.line(p = vect(50,50,50), d = vect(99,99,99))
        self.assertTrue(line1.includes(vect(23,23,23)))
        self.assertTrue(line2==line1)
        self.assertEqual(line1,line2)

        #---
        line3 = geo.line(p = (0,0,0), d = (1,1,1))
        line4 = geo.line(p = (50,50,50), d = (99,99,99))
        self.assertTrue(line3.includes(vect(23,23,23)))
        self.assertTrue(line4==line3)
        self.assertEqual(line3,line4)
        self.assertEqual(line1,line4)
        self.assertTrue(line2==line3==line1)

    def test_class_plane(self):
        # intersection :
        plane1 = geo.plane(n='2 1 -1', p = '1 2 1')
        plane2 = geo.plane(n='1 -1 1', p = '3 1 1')
        line00 = plane1.intersection(plane2)
        resultLine00 = geo.line(p = '2 -1 0' , d = '0 -3 -3')
        self.assertEqual(resultLine00,line00)
        line01 = geo.line(p = '3 4 5' , d = '1 2 2')
        plane3 = geo.plane(n='1 1 1', p = '1 1 15')
        self.assertEqual(plane3.intersection(line01),vect('4 6 7'))
        #equality :
        self.assertEqual(geo.plane(n=vect(1,3,2), p = '4 5 3'),geo.plane(n='2 6 4', p = (1,1,10.5)))
        
        # include :
        self.assertTrue(geo.plane(n='2 1 -1', p = '1 2 1').includes(vect(1,2,1)))
        self.assertTrue(geo.plane(n='2 1 -1', p = '1 2 1').includes(vect(1.5,0,0)))
        self.assertTrue(geo.plane(n='2 1 -1', p = '1 2 1').includes(geo.line((1,2,1),(1.5,0,0))))

        # distance :
        self.assertEqual(geo.plane(n='2 1 -1', p = '1 2 1').distance(vect(1,2,1)),0)
        self.assertEqual(geo.plane(n='2 1 -1', p = '1 2 1').distance(vect(1.5,0,0)),0)
        self.assertEqual(geo.plane(n='2 1 -1', p = '1 2 1').distance(geo.line((1,2,1),(1.5,0,0))),0)
        self.assertEqual(geo.plane(n='0 0 1', p = [0,0,0]).distance(geo.plane(n=[0,0,157],p=[0,0,15])),15)

        # equation :
        self.assertEqual(plane3.intersection(line01),line01.intersection(plane3))
        self.assertEqual(geo.plane('x + y + z = 10'), geo.plane('5x + 5y + 5z = 50'))
        self.assertEqual(geo.plane('x + y + z = 10'), geo.plane(n= '1 1 1', p = '1 1 8'))
        self.assertEqual(geo.plane('5x + 5y + 5z = 50'), geo.plane(n= '193 193 193', p = '1 1 8'))
        self.assertEqual(geo.plane('-12x -10y + z = 10'), geo.plane(n= '-12 -10 1', p = '0 0 10'))

        # plane constructor : intersecting lines form :
        l1 = geo.line(p=(1,3,4),d=(1,5,9))
        l2 = geo.line(p=(1,3,4),d=(3,4,7))
        self.assertEqual(geo.plane(l1,l2),geo.plane(normal = vect(-1, 20, -11), point = vect(1.0, 3.0, 4.0)))

    #---#---#---#    

    def test_class_segment(self):

        s1 = geo.segment('1 2', '6 0')
        s2 = geo.segment('3 1', '7 8')
        self.assertEqual(s1.intersection(s2),vect(3.0930232558139537, 1.1627906976744187, 0.0))

if __name__ == '__main__':
    unittest.main()
