import importlib

try:
    from .vector import vector as vect
    import utilities as vut
except:
   vect = importlib.import_module('vector').vector
   import utilities as vut
# section formula for two vectors 
def divider(a,b,m,n):
    p = (((m*b)+(n*a))/(m+n))
    return p

def distance(a,b):
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
    area_line(a,b)
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
def area_polygon(*args):
    
    """
    area_polygon(*args)
    ---
    - args : position vectors of all the vertices in a clockwise manner

    - returns : signed area under the polygon formed by the vertices
    please enter the position vectors in a consecutive and clockwise manner.

    - if arguments are given in anti-clockwise manner, then area will be equal
    to negative of the area of the polygon formed by the vertices

    """

    l = len(args)

    TotalArea = area_line(args[l-1],args[0])
    
    # here, I got confused due to range() function i wrote range(0,l-2,1) earrlier!
   
    # NOTE: remember, range stops BEFORE the last number specified in it.
    
    for idx in range(0,l-1,1):
        TotalArea += area_line(args[idx],args[idx+1])
        print(TotalArea)
    return TotalArea

a = vect(0,0)
b = vect(0,2)
c = vect(2,0)
ap = area_polygon(a,b,c)
print(ap)