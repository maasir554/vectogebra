
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

    def __init__(self,p1 : vect or tuple or list = None,p2 : vect or list = None,**kwargs) :
        
        # NEW : now line object can be constructed using list or tuples also.

        if type(p1) == type(p2) == vect :
            a = p1
            b = p2
        elif type(p1) == type(p2) == tuple or type(p1) == type(p2) == list :
            a = vect(p1[0],p1[1],p1[2])
            b = vect(p2[0],p2[1],p2[2])
        elif p1 == p2 == None :
            a = None
            b = None
        # ---
        
        # Point-direction form :
        
        if a != None and b != None :
            self.direction = b-a 
            self.point = a

        # two-point form :

        #---
        if 'point' in kwargs :
            p = kwargs['point']
        if 'p' in kwargs :
            p = kwargs['p']
        if 'pt' in kwargs :
            p = kwargs['pt']
        #---
        if 'direction' in kwargs :
            d = kwargs['direction']
        if 'd' in kwargs :
            d = kwargs['d']
        if 'dir' in kwargs :
            d = kwargs['dir']
        #---
        
        if p != None and d != None :
            if type(p) == vect:
                self.point = p
            elif type(p) == list or type(p) == tuple :
                self.point = vect(p)
            #---
            if type(d) == vect:
                self.direction = d
            elif type(d) == list or type(d) == tuple :
                self.direction = vect(d)



        # shorthands :
        self.p = self.point
        self.pt = self.point

        self.d = self.direction
        self.dir = self.direction
    
    def __type__(self):
        return "line"

    def __str__(self):
        return "line : point = " + str(self.point) + " , direction = " + str(self.direction) 


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


    # function to check if the given two lines are parallel
    def parallel(self,other) :
        """
        Function to check if the given two lines are parallel.

        ---

        argument : line object.

        ---

        Returns : True if the lines are parallel, False otherwise.

        """
        if (self.direction^other.direction).magnitude == 0 :
            return True
        else :
            return False
    
    #function to find  shorest distance between two skew lines, parallel lines, or between a line and a point. 
    def distance(self,other) :
        """
        Function to find shortest distance between two lines(skew or parallel), or between a line and a point.

        ---

        Argument : `line` object or position vector of a point

        ---

        Returns : shortest distance

        """
        if type(other) == type(self) :   
            if self.parallel(other) == False :   
                return abs((self.point-other.point)*(vut.unit_vector(self.direction^other.direction)))
    
            elif self.parallel(other) == True : 
                a1 = self.point 
                b1 = self.direction 
                a2 = other.point
                disp = a1 -a2
    
                if b1.magnitude != 0 :    
                    return ((disp ^ b1)/(b1.magnitude)).magnitude
                else :
                    raise ValueError("Direction vector cannot be zero.")

        # distance between a line and a plane :
        elif type(other) == plane :
            line0 = self
            plane0 = other
            # ---
            a = line0.point
            b = line0.direction
            # ---
            p = plane0.point
            n = plane0.normal
            # ---
            d = (a-p)*(vut.unit_vector(n))
            # ---
            if abs(n^b) == 0 :
                return 0
            else :
                return abs(d)
            


        # if other is a point:
        elif type(other) == vect:
            a = self.point
            b = self.direction
            p = other
            return (p-a)^(b/b.magnitude)


    
    # function to check if two lines intersect or not :
    def intersects(self,other) :
        """
        Function to check if two lines intersect or not. OR a line and a point intersects or not.

        ---

        argument : another `line` object. OR a point (`vector`)

        ---

        Returns : True if the lines intersect, False otherwise.

        """
        # The previous logic was wrong, as it ignored skew lines.
        if self.distance(other) == 0 :
            return True
        else :
            return False

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

        else:
            return None

    # dunder methods
    
    # function for equality of two lines :
    def __eq__(self,other) :
        """
        Function to check if two lines are equal.

        ---

        argument : another `line` object.

        ---

        Returns : True if the lines are equal, False otherwise.

        """
        L1 = self
        L2 = other

        a1 = self.point
        b1 = self.direction

        a2 = other.point
        b2 = other.direction

        if L1.includes(a2) and L2.includes(a1) and L1.parallel(L2) :
            return True
        else :
            return False


# defining class plane :
class plane(object) :
    """
    Class to define a plane.

    ---

    ### Methods of defining a plane : 
    #### 1. by a point and a normal vector :
    ```
    plane(point=(x,y,z),normal=(a,b,c))
    ```    
       
    - vector object or list of componens can also be used instead of tuples.
    - instead of `point`, `p` or `pt` can also be used.
    - instead of `normal`, `n` or `norm` can also be used.

    #### 2. by three points :
    ```
    plane((x1,y1,z1),(x2,y2,z2),(x3,y3,z3))
    ``` 
    - vector `vectogebra.vector(x,y,z)` object or lists of components `[x,y,z]` can also be used instead of tuples.
    ---

    Attributes :
        - `point` : position vector of the point on the plane.
        - `normal` : normal vector of the plane.

    ---

    """
    def __init__(self,p1=None,p2=None,p3=None,**kwargs) :
        
        # initializing the attributes :
        self.point = vect(0,0,0)
        self.normal = vect(0,0,0)

        # initializing the attributes with the values passed as arguments :
        if 'point' in kwargs :
            p = kwargs['point']
        if 'p' in kwargs :
            p = kwargs['p']
        if 'pt' in kwargs :
            p = kwargs['pt']
        
        #---

        if 'normal' in kwargs :
            n = kwargs['normal']
        if 'n' in kwargs :
            n = kwargs['n']
        if 'norm' in kwargs :
            n = kwargs['norm']
        #---

        if type(p)==vect:
            self.point = p
        elif type(p) == list or type(p) == tuple :
            self.point = vect(p)
        else :
            pass
        
        #---

        if p1 != None and p2 != None and p3 != None :
            if type(p1) == vect :
                v1 = p1
            elif type(p1) == list or type(p1) == tuple :
                v1 = vect(p1)
            if type(p2) == vect:
                v2 = p2
            elif type(p2) == list or type(p2) == tuple :
                v2 = vect(p2)
            if type(p3) == vect:
                v3 = p3
            elif type(p3) == list or type(p3) == tuple :
                v3 = vect(p3)
            
            self.point = v1
            self.normal = (v2-v1)^(v3-v1)

                

        #---

        if type(n)==vect:
            self.normal = n
        elif type(n) == list or type(n) == tuple :
            self.normal = vect(n)
        else :
            pass
        
        #---
        
        # shorthands :
        self.p = self.point
        self.pt = self.point
        
        self.n = self.normal
        self.norm = self.normal


    #------------+-----------------+--------------# 
    #------------| DUNDER METHODS  |--------------# 
    #------------+-----------------+--------------# 
    
    def __repr__(self) :
        return "Plane in 3D space : \npoint : {} \nnormal : {} \n[class plane from module vectogebra.geometry] ".format(self.point,self.normal)

    def __str__(self) :
        return "plane(normal = {}, point = {})".format(self.normal,self.point)

    # equality of two planes :
    def __eq__(self,other) :
        # two planes are equal id their normal vectors are parallel(or anti-parallel)
        # and if they have (atleast)one point in common.
        # ---
        if self.normal^other.normal == 0 :
            if self.includes(other.point):
                return True
            else :
                return False 
        else :
            return False
    
    
    #------------+----------------------+--------------# 
    #------------| IMPORTANT UTILITIES  |--------------# 
    #------------+----------------------+--------------# 


    def includes(self,arg:vect or tuple or list or line):
        """
        Function to check :
        1. if a point is on the plane, or
        2. if a line is completely on the plane.

        ---

        argument : can be any of the following : 
        1. a point in 3D space.(vector or list/tuple of components)
        2. a line in 3D space.(line object)

        ---

        Returns : True if the point is on the plane, False otherwise.

        """
        point = None
        line0 = None

        #---

        if type(arg)==vect:
            point = arg
        elif type(arg) == list or type(arg) == tuple :
            point = vect(arg)

        #---

        if type(arg) == line:
            line0 = arg

        #---
        if point !=None and abs(self.normal^(point-self.point)) == 0 :
            return True
        # a line is said to be contained in a plane if : 
        # 1. the direction of it is perpendicular to the normal vector of the plane.
        # 2. the line and the plane have atleast one point in common.
        elif line0 != None and  line0.direction*self.normal == 0 :
            # the following is the condition required while solvinf equation of a line and a plane.
            # the quantities which are crosseed must be proportional to each other. that's why the cross product is ZERO.
            return abs((line0.point*(self.normal - self.point))^(line0.direction*(self.normal - self.point))) == 0
        else :
            return False
    
    
    def contains(self,arg:vect or tuple or list or line) :
        return self.includes(arg)



