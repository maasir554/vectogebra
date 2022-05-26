"""
    Utitlity functions for vector(x,y,z)
    ----------------------------------------------------------

    file under vectogebra - python module for vector algebra

    ----------------------------------------------------------

    vectogebra/src/utilities.py

    -------------------------
    This module contains the utility operations for vasious calculation related to vectors.
    
    requires: vectogebra/src/vector.py to be imported
    
    depends on: 
    1. vectogebra/src/vector.py
    2. math module 
    -------------------------------------------------
    copyright: (C) 2022 Mohammad Maasir
    license: MIT License (see LICENSE in project's main directory)
    -------------------------------------------------
    date created: 9th of May, 2022 (3:09 AM)
    last modified: 9th of May, 2022
    -------------------------------------------------

    contributor(s): Mohammad Maasir

    -------------------------------------------------

    github: github.com/maasir554/vectogebra/vectogrbra/utilities.py

    ----------------------------------------------------------------

    report an issue : https://github.com/maasir554/vectogebra/issues
    
    ---------------------------------------------------------------------
    
    email: maasir554@gmail.com

    ---------------------------------------------------------------------

    

"""

# ------------------------------------------------------(result of a lot of research, trial and error)
# sys.path is where python search for modules.

import pathlib
import sys

currentDIR = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentDIR))
# ------------------------------------------------------  (added the src/vectogebra to the path for the test file to work)


# importlib is imported for making imports easier.


import importlib


# importing math for trigonometric and inverse trigonometric functions :-


import math


# importing vector class from vector.py


try:
    from .vector import vector as v
except:
   v = importlib.import_module('vector').vector
#    from vector import vector as v

# print(v)
# print(v(1,1,1)*v(2,2,2))

# NOTE: the type of vector will also be reffered as alias i.e. in this case, v only.
# example: a = v(1,2,3)
# print(type(a) == v) => This will return True. NOTE: do NOT use "v" or 'v' or vector.v ,
# just use alias as it is i.e.: v
# if we would have taken alias as vect then we would refer to it as vect only. and not "vect" or 'vect' or vector.vect
# if we did not had used alias, then we would refer to it as vector.vector
# Please don't get confused when working outside this module. there will be different conventions.

##########################################################

############# _____  ANGLE RELATED _____ ##################

##########################################################

# for angle between two vectors options : "radians"(default) or "degrees"
def angle(v1, v2, format="radians"):
    # python is bad at multipilcation of irrational numbers hence, we use magnitude_square()
    # instead of magnitude() (as magnitude_squared is defined separately, without use of square roots.)
    # else we  get errors like 5.99999999999999999 != 6 xD
    if (v1*v2)**2 != (v1.magnitude_squared)*(v2.magnitude_squared) and type(v1) == type(v2) == v:
        if format == "radians":
            return math.acos((v1 * v2) / (v1.magnitude * v2.magnitude))
        elif format == "degrees":
            return math.degrees(math.acos((v1 * v2) / (v1.magnitude * v2.magnitude)))
        else:
            raise ValueError("third argument must be either 'radians' or 'degrees'")
    elif (v1*v2)**2 == (v1.magnitude_squared)*(v2.magnitude_squared) and type(v1) == type(v2) == v:
        return 0.0
    else :
        raise TypeError("First two arguments must be vectors and optionally, third argument must be either 'radians' or 'degrees'")

# function to check if the tow vectors are perpendicular or not
def is_perpendicular(v1, v2):
    if angle(v1, v2, 'degrees') == 90.0:
        return True
    else:
        return False


# function to check if the tow vectors are parallel or not
def is_parallel(v1, v2):
    if angle(v1, v2, 'degrees') == 0.0:
        return True
    else:
        return False


# function to obtain unit vector from a given vector
def unit_vector(v):
    if v.magnitude != 0 :
        return (v / v.magnitude)
    else:
        return v # zero vector has arbitrary direction.

def direction(v):
    return unit_vector(v)


###########################################################

################_________ ALGEBRA _______###################

###########################################################

# addition of n vectors
def add(*args):
    v0 = v(0, 0, 0)
    for i in args:
        if type(i) == v:
            v0 = v0 + i
        elif type(i) != v:
            print(type(i))
            print(type(v))
            raise TypeError(type(v), type(i), "Arguments must be vectors")
        else:
            return 'Something went wrong :-('
    return (v0)


# function for dot product
def dot(v1, v2):
    return v1 * v2


# function for cross product
def cross(v1, v2):
    return v1 ^ v2


# magnitude of a vector or a number
def magnitude(v):
    if type(v) == v:
        return v.magnitude
    elif type(v) == int or type(v) == float:
        return (v ** 2) ** 0.5
    else:
        raise TypeError("Argument must be a vector or a number")

def proportional(a:v or tuple or list,b:v or tuple or list)->bool:
    if type(a) == v:
        v1 = a
    else :
        v1 = v(a)

    if type(b) == v:
        v2 = b
    else:
        v2 = v(b)

    return abs(v1 ^ v2) == 0


###########################################################

################_________ GEOMETRY _______##################

###########################################################

# function to find area of parallelogram formed by two vectors
def parallelogram_area(a, b):
    return a.magnitude * b.magnitude * math.sin(angle(a, b, 'radians'))


# function to find volume of parallelopiped formed by three vectors or box product
def box(a, b, c):
    return a * (b ^ c)


# function to check if three vectors are coplanar
def coplanar(a, b, c):
    if box(a, b, c) == 0:
        return (True)
    else:
        return (False)


# scalar component of vector a along the direction of vector b or opposite to direction of vector b(if the angle is
# obtuse)
def scalar_component_collinear(a, b):
    if type(a) == v and type(b) == v:
        return a * unit_vector(b)
    else:
        raise TypeError("Arguments must be vectors")


# vector component of vector a along the direction of vector b or opposite to direction of vector b(if the angle is
# obtuse)
def vector_component_collinear(a, b):
    return a * unit_vector(b) * unit_vector(b)


# scalar component perpendicular to direction of vector b
def scalar_component_perpendicular(a, b):
    return (a ^ b) / b.magnitude


# vector component perpendicular to direction of vector b
def vector_component_perpendicular(a, b):
    return scalar_component_perpendicular(a, b) * unit_vector(b ^ (a ^ b))  # Thumb rule logics***


###########################################################

#############________ EXPORT A VECTOR _______##############

###########################################################


# dictionary from a vector 
def vector_to_dict(v):
    return {'x': v.x, 'y': v.y, 'z': v.z}


# list from a vector (it will contain its coordinates/components)
def vector_to_list(v):
    return [v.x, v.y, v.z]  # returning a list of coordinates/components arranged in order of x,y,z


# tuple from a vector (it will contain its coordinates/components)
def vector_to_tuple(v):
    return v.x, v.y, v.z

def vector_to_polar(v, plane="xy", atype="deg"):
    if plane == "xy" and atype == "deg" or atype == "degree": 
        return (v.magnitude, v.angle_x_deg)
    elif plane == "xy" and atype == "rad" or atype == "radian":
        return (v.magnitude, v.angle_x)
    elif plane == "xz" and atype == 'rad'or atype == 'radian':
        return (v.magnitude, v.angle_degrees_x)
    elif plane == "xz" and atype == 'deg'or atype == 'degree':
        return (v.magnitude, v.angle_x_deg)
    elif plane == "yz" and atype == 'rad'or atype == 'radian':
        return (v.magnitude, v.angle_degrees_y)
    elif plane == "yz" and atype == 'deg'or atype == 'degree':
        return (v.magnitude, v.angle_y_deg)
    else:
        raise ValueError("plane must be either 'xy', 'xz' or 'yz'")

###########################################################

############# CREATION OF VECTOR  #########################

###########################################################

# vector from a dictionary
def dict_to_vector(d):
    if type(d) == dict:
        return v(d['x'], d['y'], d['z'])
    else:
        raise TypeError("Argument must be a dictionary")


# vector from a list


def list_to_vector(l):
    if type(l) == list:

        return (v(l[0], l[1], l[2]))

    else:

        raise TypeError("Argument must be a list")


# vector from a tuple

def tuple_to_vector(t):
    if type(t) == tuple:
        return v(t[0], t[1], t[2])
    else:
        raise TypeError("Argument must be a tuple")


# 2d vector from polar coordinates


def polar_to_vector(r, theta, atype="rad"):
    if atype == "rad" or atype == "radians" or atype == "radian"  :                    
        if round(math.cos(theta),10) != 0.0 and round(math.sin(theta),10) != 0.0:
            return v(r*math.cos(theta), r*math.sin(theta))
        elif round(math.cos(theta),10) ==0.0:
            return v(0, r*math.sin(theta))
        elif round(math.sin(theta),10) ==0.0:
            return v(r*math.cos(theta), 0)
        
    elif atype == "deg" or atype == "degrees" or atype == "degree"  :
        phi = math.radians(theta)
        if round(math.cos(phi),10) != 0.0 and round(math.sin(phi),10) != 0.0:
            return v(r*math.cos(phi), r*math.sin(phi))
        elif round(math.cos(phi),10) ==0.0:
            return v(0, r*math.sin(phi))
        elif round(math.sin(phi),10) ==0.0:
            return v(r*math.cos(phi), 0)
          
    else:
        raise ValueError("Third argument must be either 'radians' or 'radian' or 'rad' or 'degrees' or 'degree' or 'deg'")


# print(polar_to_vector(1, 2*math.pi/2))
# print(polar_to_vector(1,3*math.pi/2))
# print(polar_to_vector(1,4*math.pi/2))
# print(polar_to_vector(1,5*math.pi/2))


