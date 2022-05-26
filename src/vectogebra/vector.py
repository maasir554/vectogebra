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
    # may us *args and *kwargs method later but as of now i dont have time
    #it is a WAY better method in some cases.!
    
    def __init__(self, i=0, j=0, k=0):      # component will take value 0 if not specified. 
        #Rectangular Components in i,j,k
        if (type(i) == int or type(i) == float) and (type(j) == int or type(j) == float) and (type(k) == int or type(k) == float):
            self.i = i
            self.j = j
            self.k = k
        elif type(i) == list:
            self.i = i[0]
            self.j = i[1]
            self.k = i[2]
        elif type(i) == tuple:
            self.i = i[0]
            self.j = i[1]
            self.k = i[2]
        elif type(i) == dict :
            if 'i' in i and 'j' in i and 'k' in i:
                self.i = i['i']
                self.j = i['j']
                self.k = i['k']
            elif 'x' in i and 'y' in i and 'z' in i:
                self.i = i['x']
                self.j = i['y']
                self.k = i['z']
            else:
                raise ValueError("Invalid input")
        elif type(i) == str:
            lst = i.split(' ')
            if len(lst) == 3:
                    self.i = float(lst[0])
                    self.j = float(lst[1])
                    self.k = float(lst[2])
            else:
                raise ValueError("Invalid input")
        elif type(i) == type(None) :
            raise ValueError("Invalid input : None can not be used to construct a vector object.")



        
        #Rectangular Components in x,y,z
        self.x = self.i
        self.y = self.j
        self.z = self.k
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
        self.direction = self.unit_vector

        self.type = self.__type__()

        #angle made by vector with the coordinate axes x,y and z respectively :
        if self.magnitude != 0:    
            self.angle_x = math.acos(self.i/self.magnitude)
            
            self.angle_y = math.acos(self.j/self.magnitude)
            
            self.angle_z = math.acos(self.k/self.magnitude)
        else:
            self.angle_x = 0
            self.angle_y = 0
            self.angle_z = 0
        # degrees:
        self.angle_x_deg = self.angle_x * 180 / math.pi
        self.angle_y_deg = self.angle_y * 180 / math.pi
        self.angle_z_deg = self.angle_z * 180 / math.pi


        # --- CONVERSIONS ---

        # list of components :
        self.list = [self.i, self.j, self.j] 

        # dictionary of components :
        self.dict = {'x':self.i, 'y':self.j, 'z':self.k}
        
        # tuple of components :
        self.tuple = (self.i, self.j, self.k)

        
        

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
            return(self.__unit_vector)
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
    # if scalar number is wrritten in the beging, we uses __rmul__ overloader [Magic Method]
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

    # round() function / method defination:-
    def __round__(self,other = 0) :
        if type(other) == int:
            return(vector(round(self.i,other),round(self.j,other),round(self.k,other)))
        else:
            return("Error: Invalid input")

    def __abs__(self):
        return(self.magnitude)

    ########### More Dunder methods / Magic methods to be added #############


    # Unary operator overloading :-
    # NOTE : + is the unary plus operator in this case
    def __pos__(self):
        return self
    # NOTE : - is the unary minus operator in this case
    def __neg__(self):
        return vector(-self.i, -self.j, -self.k)



# i will write i cap as i_

