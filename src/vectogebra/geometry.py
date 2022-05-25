
#----------------------------------------------------------------
import pathlib
import sys

currentDIR = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentDIR))
#----------------------------------------------------------------

import importlib

try:
    from .vector import vector as vect
    import utilities as vut
except:
   vect = importlib.import_module('vector').vector
   vut = importlib.import_module('utilities')
# section formula for two vectors 
def divider(a,b,m,n):
    p = (((m*b)+(n*a))/(m+n))
    return p

def distance(a : vect,b : vect):
    if type(a) == type(b) == vect :

        return (b-a).mod
    else :
        raise TypeError("distance() takes two vectors as arguments")

# area of a triangle formed by theree position vector as its vertices
def area_triangle(a,b,c):
    if type(a) == type(b) == type(c) == vect :
        p = a - b  
        r = c - b
        return ((r^p).mod)/2
    else :
        raise TypeError("area_triangle() takes three vectors as arguments")

# area under a line segment joining two vectors (2d only)):
# area bounded by line on x axis:
# negative area is allowed in case of vectors
def area_line(a,b):
    """ 
    ### area_line(a,b)
    - a and b : position vectors
    - returns signed area under the line segment joining a and b falling on x axis 
    - if b.x > a.x then area will be +ve
    - if b.x < a.x then area will be -ve
    """
    if type(a) == type(b) == vect :
         return ((b.x - a.x)*(a.y+b.y))/2
    else :
        raise TypeError("area_line_x() takes two vectors as arguments")

# enter the position vectors of all the vertices in a clockwise manner :
def area_polygon(*args : vect):
    
    """
    ### area_polygon(*args) - 2D only.
    
    - args : position vectors of all the vertices in a clockwise manner

    - returns : signed area under the polygon formed by the vertices
    please enter the position vectors in a consecutive and clockwise manner.

    - if arguments are given in anti-clockwise manner, then area will be equal
    to negative of the area of the polygon formed by the vertices

    - if you have a list of arguments, you can pass them as:
        list1 = [v1 ,v2 ,v3, ...]
        area_polygon(*list1)


    """

    l = len(args)

    TotalArea = area_line(args[l-1],args[0])
    
    # here, I got confused due to range() function i wrote range(0,l-2,1) earrlier!
   
    # NOTE: remember, range stops BEFORE the last number specified in it.
    
    for idx in range(0,l-1,1):
        TotalArea += area_line(args[idx],args[idx+1])
    return TotalArea


#to check if the given points are coplanar :-
def coplanar(*args : vect):
    """
    To check if the given points are coplanar or not.
    
    ---
    
    args : position vectors of all the points whose coplanarity is to be verified.
    
    ---

    Returns : 
        - True : if the points are coplanar
        - False : if the points are not coplanar

    """

    l = len(args)
    
    # choosing args[0] as the reference vector.
    
    # making a list of displacement vectors of points oyther than args[0] w.r.t. args[0] 

    if l >= 3 :
        dispVectors = []
        for i in args :
            if i !=args[0] :
                dispVectors.append(args[0]-i)
        else :
            pass
        
        # default return value of the function : True
        returnValue = True
        # checking the directions of cross products of displacement vectors  
        # with the reference vector as R = dispVectors[0]^dispVectors[1]
        R = dispVectors[0]^dispVectors[1]
        for i in dispVectors[1 : len(dispVectors)] :  

            if (i^dispVectors[0]).magnitude != 0 :
                if (vut.unit_vector(i^dispVectors[0]) != vut.unit_vector(R) ) and ( vut.unit_vector(i^dispVectors[0]) != -vut.unit_vector(R) ) :
                    returnValue = False
                    break
                else :
                    pass
            else : 
                pass      
        return returnValue
    else :
        return True # as three points are always coplanar in sD space.


# function to find centroid of a polygon :
def centroid(*args : vect):
    """
        Function to find centroid of a polygon.

        ---

        args : position vectors of all the vertices of the polygon whose centroid is to be calculated.

        ---

        Returns : position vector of the centroid of the polygon.

        ---

        Copyright © 2022 Mohammad Maasir 

    """
    l = len(args)
    S = vect(0,0,0)
    for i in args :
        S += i
    G = S/l
    return G


# ------------------------------------------------------------------
# . . . . . . . . . IMPORTANT GEOMETRY CLASSES . . . . . . . . . . . 
# ------------------------------------------------------------------

class line:
    """
    Python class for line in a 3D space.

    ---
    
    ## Methods to define a line : -
    ### 1. Point-direction form 
    Syntax : `line(point = vector(x,y,z), direction =vector(a,b,c) )`

    - you also can write `p`  or `pt`  instead of `point` 

    - and `d` or `dir` or `dr` instead of `direction` 
    
    ### 2. Two-points form 
    Syntax : ` line(a,b) `
    - here, `a` and `b` are position vectors of the two points through which the line is passing.
    """

    def __init__(self,a : vect = None,b : vect = None,**kwargs) :
        
        # Point-direction form :
        
        if a != None and b != None :
            self.direction = b-a 
            self.point = a

        # two-point form :

        if (a == None and b == None) and ('point' in kwargs) and ('direction' in kwargs) :
            self.direction = kwargs['direction']
            self.point = kwargs['point']

        if (a == None and b == None) and ('p' in kwargs) and ('d' in kwargs) :
            self.direction = kwargs['d']
            self.point = kwargs['p']

        if (a == None and b == None) and ('pt' in kwargs) and ('dir' in kwargs) :
            self.direction = kwargs['dir']
            self.point = kwargs['pt']
    
    
    def __type__(self):
        return "line"


    # function to check if the line includes (or passes through) a point :
    def includes(self,r : vect) :
        """
        Function to check if the line includes (or passes through) a point.

        ---

        argument : position vector of the point whose inclusion is to be checked.

        ---

        Returns : True if the line includes the point, False otherwise.

        """
        # by equation r = a + t*b {t is an arbitrary scalar number}
        # we have (r-a) = t*b
        # that means (r-a) should be proportional to b (direction vector)
        # as cross product of propotional vectors (either parallel or anti-parallel) is 0, 
        # we have :-

        if (r-self.point)^self.direction == 0 :
            return True
        else :
            return False


    # function to check if two lines intersect or not :
    def intersects(self,other) :
        """
        Function to check if two lines intersect or not.

        ---

        argument : another line object.

        ---

        Returns : True if the lines intersect, False otherwise.

        """
        # extracting vectors from the lines :
        # ---
        P1 = self.point
        D1 = self.direction
        # ---
        P2 = other.point
        D2 = other.direction
        # ---
        # --- --- --- 
        
        # extracting the components of vectors defined above.
        # ---
        p = P1.x
        q = P1.y
        r = P1.z
        # ---
        s = D1.x
        t = D1.y
        u = D1.z
        # ---
        # ---
        a = P2.x
        b = P2.y
        c = P2.z    
        # ---
        f = D2.x
        g = D2.y
        h = D2.z
        # ---
        # --- --- ---
        
        # by mathematical calculations following condition is observed :
        if (f*t != s*g) or (u*f != s*h) or (u*g != t*h) :
            return True
        else :
            return False
        
        # this took me 2 hours to figure out the logic !

    def intersection(self,other) :
        """
            Function to find the position vector of the intersection point (if exists), of two lines.

            ---

            The argument should also be a line object.
        """
        # extracting vectors from the lines :
        # ---
        P1 = self.point
        D1 = self.direction
        # ---
        P2 = other.point
        D2 = other.direction
        # ---
        # --- --- --- 

        # extracting the components of vectors defined above.
        # ---
        p = P1.x
        q = P1.y
        r = P1.z
        # ---
        s = D1.x
        t = D1.y
        u = D1.z
        # ---
        # ---
        a = P2.x
        b = P2.y
        c = P2.z    
        # ---
        f = D2.x
        g = D2.y
        h = D2.z
        # ---
        # --- --- ---
        if self.intersects(other) : 
            if (f*t) != (s*g) :
                phi = ((t*(p-a))-(s*(q-b)))/((f*t)-(s*g))
            elif (u*f) != (s*h) :
                phi = ((u*(p-a))-(s*(r-c)))/((u*f)-(s*h))
            elif (u*g) != (t*h) :
                phi = ((u*(q-b))-(t*(r-c)))/((u*g)-(t*h))
            else :
                raise ValueError("Error in function line.intersects().")

            INTERSECTION = P2 + (phi*D2)
            return INTERSECTION

        else : 
            if (s/f) == (t/g) == (u/h) :
                print("The lines are parallel !")
                return None
            else :
                print("The lines are skew lines !")
                return None
        # this function in not fully perfect as it an not yet detect skew lines.
        # it will still work for the lines that intersects each other
        # and th function intersects() is also not perfect. it can not detect skew lines

