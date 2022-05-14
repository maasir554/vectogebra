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

