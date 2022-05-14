try:
    from .vector import vector as vect
    import utilities as vut
except:
   from vector import vector as vect
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

a = vect(0,2)
b = vect(2,0)
c = vect(0,0)
print(area_triangle(a,c,b))