"""
    file under vectogebra - python module for vector algebra
    
    vectogrbra/__init__.py
    -------------------------
    This module contains the 'vector' class.
    -------------------------------------------------
    copyright: (C) 2022 Mohammad Maasir
    license: MIT License (see LICENSE in project's main directory)
    -------------------------------------------------
    date created: 9th of May, 2022 (3:09 AM)
    last modified: 9th of May, 2022
    -------------------------------------------------
    contributor(s): Mohammad Maasir
    -------------------------------------------------
    github: github.com/maasir554

"""

# importing vector class from vector.py
# the dot is necessary to avoid name conflict. 
# from .vector import vector

# exception handling is best solution to any problem
# here in
try:
    from .vector import vector  # this import is for the build version
except :
    pass        # simply ignore the error and the module will be imported 
# pass will simply ignore the import command here and test files will import the module by
# the local command written in them


"""
    to use vector object class, in your file, write: import vectogerbra.vector as v
    then you can use the vector class in your file
    example: v1 = v(1,2,3)

    to import the vector class in your file, you can use the following:
    ## import vectogerbra.vector as v [or any other alias name you want]
    ## from vectogerbra import vector as v [or any other alias name you want]
"""

# importing utility functions from utilities.py

# from .utilities import *

