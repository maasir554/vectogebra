
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
        a = None
        b = None
        
        if p1 != None and p2 != None :
            if type(p1) == vect :
                a = p1
            else :
                a = vect(p1)
            # ---
            if type(p2) == vect :
                b = p2
            else :
                b = vect(p2)

        # Point-direction form :
        
        if a != None and b != None :
            self.direction = b-a 
            self.point = a

        # two-point form :

        #---
        if 'point' in kwargs :
            p = kwargs['point']
        elif 'p' in kwargs :
            p = kwargs['p']
        elif 'pt' in kwargs :
            p = kwargs['pt']
        else :
            p = None
        #---
        if 'direction' in kwargs :
            d = kwargs['direction']
        elif 'd' in kwargs :
            d = kwargs['d']
        elif 'dir' in kwargs :
            d = kwargs['dir']
        elif 'dr' in kwargs :
            d = kwargs['dr']
        else :
            d = None
        #---
        
        if p != None and d != None :
            if type(p) == vect:
                self.point = p
            elif type(p) == list or type(p) == tuple or type(p) == str or type(p) == dict:
                self.point = vect(p)
            #---
            if type(d) == vect:
                self.direction = d
            elif type(d) == list or type(d) == tuple or type(p) == str or type(p) == dict:
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

    def __repr__(self):
        return "line : point = " + str(self.point) + " , direction = " + str(self.direction) + '\n' + '[line object from vectogebra.geometry module]'


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
        if type(other) ==type(self):    
            if abs(self.direction^other.direction) == 0 :
                return True
            else :
                return False
        elif type(other) == plane :
            return (self.direction)*(other.normal) == 0 
        else :
            raise Exception("vectogebra.geometry.line.parallel() only accepts line or plane as arguments.")

    
    #function to find  shorest distance between two skew lines, parallel lines, or between a line and a point. 
    def distance(self,other) :
        """
        Function to find shortest distance between two lines(skew or parallel), or between a line and a point,
        or between a line and a plane.

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

        elif type(other) == list or type(other) == tuple or type(other) == dict or type(other) == str :
            a = self.point
            b = self.direction
            p = vect(other)
            return (p-a)^(b/b.magnitude)

        else :
            raise Exception("vectogebra.geometry.line.distance() only accepts line or plane or point as arguments.")


    
    # function to check if two lines intersect or not :
    def intersects(self,other) :
        """
        Function to check if two lines intersect or not. OR a line and a point intersects or not,
        OR a line and a plane intersects or not.

        ---

        argument : another `line` object, OR a point (`vector` or list or tuple or str : 'x y z'), OR a plane

        ---

        Returns : True if the lines intersect with other object, False otherwise.

        """
        # The previous logic was wrong, as it ignored skew lines.
        return self.distance(other) == 0 
        

    def intersection(self,other) :
        """
            Function to find the position vector of the intersection point (if exists), of two lines,
            or between a line and a plane.

            ---

            The argument should also be a line object or a plane object.
        """
        if type(other) == type(self) :    
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
        #---

        elif type(other) == plane :
            return other.intersection(self) #alredy definde in plane class.

        elif type(other) == vect:
            if self.contains(other) :
                return other
            else :
                return None
        
        elif type(other) == list or type(other) == tuple or type(other) == dict or type(other) == str :
            if self.contains(vect(other)) :
                return vect(other)
            else :
                return None

        else : 
            raise Exception("vectogebra.geometry.line.intersection() only accepts line or plane as arguments.")
        


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
    ### 3. by equation of plane :
    ```
        plane('ax + by + cz = d')
        plane('ax - by - cz = -d')
        plane('ax -by -cz = d')
        plane('-ax + by + cz = -d')
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
        elif 'p' in kwargs :
            p = kwargs['p']
        elif 'pt' in kwargs :
            p = kwargs['pt']
        else :
            p = None
        
        #---

        if 'normal' in kwargs :
            n = kwargs['normal']
        elif 'n' in kwargs :
            n = kwargs['n']
        elif 'norm' in kwargs :
            n = kwargs['norm']
        else :
            n = None

        #---

        if type(p)==vect:
            self.point = p
        elif type(p) == list or type(p) == tuple or type(p) == str or type(p) == dict:
            self.point = vect(p)
        else :
            pass
        
        #---

        if p1 != None and p2 != None and p3 != None :
            
            if type(p1) == vect :
                v1 = p1
            elif type(p1) == list or type(p1) == tuple or type(p1) == str or type(p1) == dict:
                v1 = vect(p1)
            else :
                raise TypeError("Error in constructor of plane")
            #---    
            if type(p2) == vect:
                v2 = p2
            elif type(p2) == list or type(p2) == tuple or type(p2) == str or type(p2) == dict:
                v2 = vect(p2)
            else :
                raise TypeError("Error in constructor of plane")
            #---
            if type(p3) == vect:
                v3 = p3
            elif type(p3) == list or type(p3) == tuple or type(p3) == str or type(p3) == dict:
                v3 = vect(p3)
            else :
                raise TypeError("Error in constructor of plane")
            #---
            self.point = v1
            self.normal = (v2-v1)^(v3-v1) 
        else : 
            pass

                

        #---

        if type(n)==vect:
            self.normal = n
        elif type(n) == list or type(n) == tuple or type(n) == str or type(n) == dict:
            self.normal = vect(n)
        else :
            pass
        
        #---

        # plane from its equation :
        if p1 != None and p2 == None and p3 == None and type(p1) == str :
            self.normal = PlaneEquationParser(p1)['normal']
            self.point = PlaneEquationParser(p1)['point']
        
        
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


    def includes(self,arg:vect or tuple or list or line or str or dict):
        """
        Function to check :
        1. if a point is on the plane, or
        2. if a line is completely on the plane.

        ---

        argument : can be any of the following : 
        1. a point in 3D space.(vector or list/tuple of components)
        2. a line in 3D space.(line object)

        ---

        Returns : True if the point is on the plane or line is on the plane(completely), False otherwise.

        """
        point = None
        line0 = None

        #---

        if type(arg)==vect:
            point = arg 
        elif type(arg) == list or type(arg) == tuple or type(arg) == str or type(arg) == dict:
            point  = vect(arg)

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
    
    
    def contains(self,arg:vect or tuple or list or line or str or dict) :
        return self.includes(arg)

    def distance(self, other : vect or line or tuple or list or dict or str ) -> int or float :
        """
            Function to find the distance between a plane and a point or a parallel line.

            ---

            argument : can be any of the following : 
            1. a point in 3D space.(vector or list/tuple/dict of components)
            2. a line in 3D space.(line object)

            ---

            Returns : distance between the plane and the point or parallel line.

            """
        a = None
        line0 = None
        p = self.point
        n = self.normal
        #---

        if type(other)==vect:
            a = other 
        elif type(other) == list or type(other) == tuple or type(other) == str or type(other) == dict:
            a  = vect(other)

        #---

        if type(other) == line:
            line0 = other

        #---
        if a !=None :
            return abs((a-p)*(n/n.magnitude))
        #---
        elif line0 != None :
            return line0.distance(self)
        #---
        elif type(other) == plane :
            n1 = self.n
            n2 = other.n
            p1 = self.p
            p2 = other.p
            if vut.proportional(n1,n2):
                return abs((p2-p1)*(n1/n1.magnitude))
            else :
                return 0
        #---
        else :
            return None


    def intersection(self,other : line or tuple or list or dict or str ) -> vect or line :
        """
            Function to find the intersection point between a plane and a line or a plane.

            ---

            argument : can be any of the following : 
            1. a plane in 3D space.(plane object)
            2. a line in 3D space.(line object)

            ---

            Returns : intersection point between the plane and the line or plane.

            """
        
        if type(other) == plane :
            
            n1 = self.n
            n2 = other.n
            #---
            p1 = self.point
            p2 = other.point
            #---
            
            if n1 ^ n2 !=  0:
                # we knoow that the direction of the line(intersection) is
                # perpendicular to the normal vectors of both planes. Hence, we have :
                
                b = n1 ^n2 # the direction of resulting line
                
                #---
                
                # now we need a fixed point on the line (that is common to both planes.), to completely define the line.
                # So, lets take a FIXED point on the line such that:
                # when wejoin that point(Lets name it c) with the point p1, 
                # we get a line which is perpendicular to the direction vector(i.e. b) of the line(intersection).
                # this point will be a unique point.
                # so, lets find the point c.
                # we know that the line(intersection) is perpendicular to the normal vector of the plane.
                # so, we can find the point c by :

                v = b^n1 # direction vector of the line formed by joining the fixed point(c) with the point p1.

                lmbd = ((p2 - p1)*n2)/(v*n2)    # constant of proportionality, computed by solvinf equations.  
                c = p1 + lmbd*v                 # the fixed point on the line.
                
                #---

                # finally the line is :
                return line(point = c,direction = b)
            else :
                return None
        
        #---                                        major bug fixed :-

        elif type(other) == line :

            p = self.point
            n = self.normal

            #---
            a = other.point
            b = other.direction
            #---
            if b*n != 0 :
                lmbd = ((p-a)*n)/(b*n)
                c = a + lmbd*b
                return c
            else :
                return None

        #---

        else :
            raise TypeError("vectogebra.geometry.plane.intersection : argument must be a plane or a line.")

    def parallel(self,other : line or any ) -> bool :
        """
            Function to check if the plane is parallel to a line or othe plane.

            ---

            argument : can be any of the following : 
            - a plane in 3D space.(plane object)
            - a line in 3D space.(line object)

            ---

            Returns : True or False depending on the condition.

            """
        if type(other) == plane :
            n1 = self.n
            n2 = other.n
            #---
            return abs(n1 ^ n2) ==  0
        
        elif type(other) == line :
            n = self.normal
            #---
            b = other.direction
            #---
            return n*b == 0
        else :
            raise TypeError("vectogebra -> geometry.py -> plane -> parallel : argument must be a line or a plane.")
    

# +----------------------------+
# |    PLANE EQUATION PARSER   |
# +----------------------------+
def PlaneEquationParser(eqn:str) :

    """
        Function to parse the plane equation.

        argument : 

        the plane equation in string format.
        The following equations are velid : 
        - 'ax + by + cz = d'
        - 'ax - by - cz = -d'
        - '-ax -by -cz = d'
        - '-ax + -by + -cz = -d
        - 'ax - -by - -cz = d'
        - '-ax - by - cz = -d'
        Returns : a dict containing normal and a point on the plane.

    """        
    
    
    list_eqn = eqn.split(' ')
    dict_eqn = {'x_coeff':0,'y_coeff':0,'z_coeff':0,'constant':0}

    for i in list_eqn :
        if 'x' in i :
            if len(i) != 1 :    
                if list_eqn[list_eqn.index(i)-1] == '+' :    
                    dict_eqn['x_coeff'] = float(i.replace('x',''))
                elif list_eqn[list_eqn.index(i)-1] == '-' :
                    dict_eqn['x_coeff'] = -float(i.replace('x',''))
                else :
                    dict_eqn['x_coeff'] = float(i.replace('x',''))
            else :
                dict_eqn['x_coeff'] = 1
        if 'y' in i :
            if len(i) != 1 :   
                if list_eqn[list_eqn.index(i)-1] == '+' :    
                    dict_eqn['y_coeff'] = float(i.replace('y',''))
                elif list_eqn[list_eqn.index(i)-1] == '-' :
                    dict_eqn['y_coeff'] = -float(i.replace('y',''))
                else :
                    dict_eqn['y_coeff'] = float(i.replace('y',''))
            else :
                dict_eqn['y_coeff'] = 1
        if 'z' in i :
            if len(i) != 1 :    
                if list_eqn[list_eqn.index(i)-1] == '+' :    
                    dict_eqn['z_coeff'] = float(i.replace('z',''))
                elif list_eqn[list_eqn.index(i)-1] == '-' :
                    dict_eqn['z_coeff'] = -float(i.replace('z',''))
                else :
                    dict_eqn['z_coeff'] = float(i.replace('z',''))
            else :
                dict_eqn['z_coeff'] = 1

        if '=' in i :
            dict_eqn['constant'] = float(list_eqn[list_eqn.index(i)+1])
    
    nx = dict_eqn['x_coeff']
    ny = dict_eqn['y_coeff']
    nz = dict_eqn['z_coeff']
    d = dict_eqn['constant']
    
    normal = vect(nx, ny, nz)
    # for point point :
    if nx != 0 and ny != 0 and nz != 0 : 
        px = 1
        py = 1
        pz = (d-nx-ny)/nz
        point = vect(px,py,pz)
    elif nx != 0 and ny != 0 and nz ==0:
        px = 1
        py = (d-nx)/ny 
        pz = 0
        point = vect(px,py,pz)
    elif nx != 0 and ny == 0 and nz != 0:
        px = 1
        py = 0
        pz = (d-nx)/nz
        point = vect(px,py,pz)
    elif nx == 0 and ny != 0 and nz != 0:
        px = 0
        py = 1
        pz = (d-ny)/nz
        point = vect(px,py,pz)

    return {'normal':normal, 'point':point}

