"""
    vector(x,y,z)
    ----------------------------------------------------------------

    file under vectogebra - python module for vector algebra

    ----------------------------------------------------------------

    vectogebra/src/vector.py

    ----------------------------------------------------------------

    This module contains the 'vector' class.

    ----------------------------------------------------------------
    copyright: (C) 2022 Mohammad Maasir
    license: MIT License (see LICENSE in project's main directory)
    ----------------------------------------------------------------
    date created: 8th of May, 2022 (11:45 PM)
    last modified: 8th of May, 2022
    ----------------------------------------------------------------

    contributor(s): Mohammad Maasir

    ----------------------------------------------------------------

    github: github.com/maasir554/vectogebra/vectogrbra/vector.py
    
    ----------------------------------------------------------------

    report an issue : https://github.com/maasir554/vectogebra/issues
    
    ---------------------------------------------------------------------
    
    email: maasir554@gmail.com

"""
import math


class vector:
    
    #Constructor

    def __init__(self, i, j, k):
        #Rectangular Components in i,j,k
        self.i = i
        self.j = j
        self.k = k
        #Rectangular Components in x,y,z
        self.x = i
        self.y = j
        self.z = k
        #Magnitude
        self.magnitude = self.__magnitude()  #refer to __magnitude() below
        self.modulus = self.magnitude
        self.mod = self.magnitude   
        self.mag = self.magnitude 
        #Magnitude squared
        self.magnitude_squared = self.__magnitude_squared() #refer to __magnitude_squared() below
        self.modulus_squared = self.magnitude_squared
        self.mod_squared = self.magnitude_squared
        self.mag_squared = self.magnitude_squared
        #Unit Vector [Tuple] along the vector (parallel)
        # NOTE !WARNING! the unit_vector function returns a TUPLE (x,y,z) and NOT a vector
        self.unit_vector = (self.__unit_vector())


        self.type = self.__type__()

    #String representation of the vector object :

    def __type__(self):
        return("vector")

    def __str__(self,format="default"):
        if format == "csv" or format == "tuple" or format == "default":
            return("vector({}, {}, {})".format(self.i, self.j, self.k))
        elif format == "componential" or format =="components" or format == "comp":
            return("({}i + {}j + {}k)".format(self.x, self.y, self.z))
        else:
            return("vector({}, {}, {})".format(self.x, self.y, self.z))

    def to_str(self,format="default") :
        return(self.__str__(format))

    def __repr__(self):
        return(self.__str__('default'))     # important for command line usage (when object is called without print())

    
    # Magnitude calculator

    def __magnitude(self):
        return math.sqrt((self.i)**2 + (self.j)**2 + (self.k)**2)

    # Magnitude Squared calculator

    def __magnitude_squared(self):
        return(self.i**2 + self.j**2 + self.k**2)

    # Unit vector calculator (will return simple Tuple only) the result will be a tuple of 3 numbers
    #! WARNING! This function will NOT return a vector object !

    def __unit_vector(self):
        if self.magnitude !=0:
            return(self.i/self.magnitude, self.j/self.magnitude, self.k/self.magnitude)
        else:
            return("Zero vector do not have a direction")
   
    # function to return unit_vector in different (string) formats 
    def unit_vector(self, format="default"):
        if format == "csv" or format == "tuple" or format == "default":
            return(self.unit_vector)
        elif format == "componential" or format =="components" or format == "comp":
            return("({}i + {}j + {}k)".format(self.x, self.y, self.z))

    # ALGEBRA : addition of vectors :-
    def __add__(self, other):
        return(vector(self.i + other.i, self.j + other.j, self.k + other.k))
    
    # ALGEBRA : DOT product and multiplication of vectors with scalars:-
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return(vector(self.i * other, self.j * other, self.k * other))
        elif type(other) == vector:
            return(self.i * other.i + self.j * other.j + self.k * other.k)
        else:
            return("Error: Invalid input")
    #if salar number is wrir=tten in the beging, we uses __rmul__ overloader [Magic Method]
    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return(vector(self.i * other, self.j * other, self.k * other))
        elif type(other) == vector:
            return(self.i * other.i + self.j * other.j + self.k * other.k)
        else:
            return("Error: Invalid input")

    # ALGEBRA : subtraction of vectors :-
    def __sub__(self, other):
        return(vector(self.i - other.i, self.j - other.j, self.k - other.k))

    # ALGEBRA : cross product of vectors :-
    # NOTE : ^(XOR operator) is the cross product operator in this case 
    def __xor__(self, other):
        if type(other) ==vector:
            return(vector(self.j * other.k - self.k * other.j, self.k * other.i - self.i * other.k, self.i * other.j - self.j * other.i))
        else:
            suggest = "if you have any suggestion, please suggest @ https://github.com/maasir554/vectogebra/issues"
            return("Error: Please note that the cross product is only defined for vectors. \nIn vectogebra, for any two vectors a and b, (a^b) is same as a cross b.\n" + suggest)
    
    # ALGEBRA : division by scalar
    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return(vector(self.i / other, self.j / other, self.k / other))  
        else:
            suggest = "if you have any suggestion, please suggest @ https://github.com/maasir554/vectogebra/issues"
            return("Error: Please note that division of vector by a vector is not possible. \n" + suggest)
    # ALGEBRA : raising vectors to a integral power [Inspired by JEE queations] 
    def __pow__(self, other):
        if type(other) == int  and other == 0:
            return("Error! : power must be an integer >= 1")
        elif type(other) == int and other>=1 and other%2 == 0:
            return(self.magnitude**(other))
        elif type(other) == int and other>=3 and other%2 == 1:
            return((self.magnitude**(other-1))*self)
    # Making the class iterable to perform addition of multiple vectors simultainously e.g. a+b+c OR a-b+c OR a+b-c , etc.
    def __iter__(self):
        pass

    #############################################################################################

    # LOGICAL OPERATORS : equality of two vectors :-
    def __eq__(self, other):
        if type(other) == vector:
            return(self.i == other.i and self.j == other.j and self.k == other.k) #returns true if all components are equal
        else:
            return("Error: Vectors can only be equated among themselves")   #returns false if one or both of the input(s) is/are not (a) vector(s)
    # LOGICAL OPERATORS : inequality of two vectors :-
    # NOTE : != is the inequality operator in this case
    def __ne__(self, other):
        if type(other) == vector:
            return(self.i != other.i or self.j != other.j or self.k != other.k) #returns true if one or more of the components are not equal
        else:
            return("Error: Vectors can only be compared among themselves")
    # LOGICAL OPERATORS : greater than of two vectors :-
    def __gt__(self, other):
        if type(other) == vector:
            return(self.magnitude > other.magnitude)    # comparing magnitude makes sense instead of comparing components
        else:
            return("Error: Vectors can only be compared among themselves")
    # LOGICAL OPERATORS : less than of two vectors :-
    def __lt__(self, other):
        if type(other) == vector:
            return(self.magnitude < other.magnitude)    # comparing magnitude makes sense instead of comparing components
        else:
            return("Error: Vectors can only be compared among themselves")
    # LOGICAL OPERATORS : greater than or equal to of two vectors :-
    def __ge__(self, other):
        if type(other) == vector:
            return(self.magnitude >= other.magnitude)
        else:
            return("Error: Vectors can only be compared among themselves")
    # LOGICAL OPERATORS : less than or equal to of two vectors :-
    def __le__(self, other):
        if type(other) == vector:
            return(self.magnitude <= other.magnitude)
        else:
            return("Error: Vectors can only be compared among themselves")

    ########### More Dunder methods / Magic methods to be added #############




# i will write i cap as i_