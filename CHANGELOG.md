# CHANGELOG

record of major changes to the project including bug fixes will be stored here.

## [0.0.6]

### the library is now comlpetely functional.

- optimised the directory structure.
- importing vector class is now easy.
- resolved the issue of angle between parallel vectors.

## [0.0.7]

### updates in vector class

- 2D vector can now be defined by passing two arguments and third will automatically be set to 0.
- `vector()` can now accept single argument as a list / dict or tuple of x, y, and z components.
- ### new attributes:
  1. `vector.angle_x` - angle between vector and x axis.
  2. `vector.angle_y` - angle between vector and y axis.
  3. `vctor.angle_z` - angle between vector and z axis.
     (above angles will be in radians) suffix `_deg` at the end of the attribute to get angle in degrees.
- ### define vector using string !
  vector(`x y z`) will return vector object : vector(x, y, z)

### updates in vut

- polar vectors are now supported.
  to define a vector using polar argument, use vut.polar_to_vector(r, theta, atype)
  atype can be 'deg' or 'degree' or 'rad' or 'radian' default is 'rad'. example:
  ```python
    >>> vut.polar_to_vector(1, 90, 'deg')
    >>> vut.polar_to_vector(1, math.pi/2, 'rad')
  ```
- polar exportes added
  vector can be exported to a polar representation by using the following functions:
  ```python
     vut.polar_to_vector(vector, plane, atype)
  ```
  - plane can be 'xy' or 'yz' or 'zx'
  - atype can be 'deg' or 'degree' or 'rad' or 'radian' default is 'rad'.
  - default plane is 'xy', and default atype is 'deg' in this case.
  - angle will be measured from the +ve x- axis in case of xy and yz plane, and with +ve y- axis in the case of yz plane.

### new module for geometry

this module contains functions for coordinate geometry calculations using vectors (Position Vectors).
this module is an application of vector.py and utilities.py

```python
import vectogebra.geometry as geo
```

defined the following functions :-

1. `divider(a,b,m,n)` : returns a point that divides the line segment joining `a` and `b` by in the ratio `m`:`n`.
2. `distance(a,b)` : returns the distance between `a` and `b`
3. `area_line(a,b)` : signed area under the line segment joining a and b.
4. `area_polygon` : signed area of polygon with any number of vertices.
5. `area_triangle` : area formed by a triangle with vertices `a` , `b` and `c`.

## [0.0.8]

### 1. changes in vector class

- `round()` method defined for the vector class.
- Conversions to `list` , `dict`, and `tuple` using attribute names :
  _[26 May, 2022]_
  ```python
    v = vectorgbra.vector(1,2,3)
    v.list # returns list of components in order of x, y, z.
    v.dict # returns dict of components in order of x, y, z.
    v.tuple # returns tuple of components in order of x, y, z.
  ```

### 2. changes in geometry.py mudule:

- `coplanar(*args)` function defined. this function returns `True` if the given points are coplanar. else returns `False`. - _23 May, 2022_

  [*24 May 2022*]

- `area_polygon(*args)` and `area_line(a,b)` functions defined.

- `centroid(*args)` function defined which returns the centroid of the polygon.

- Class `line` defined. this class represents a line in 3-dimensional space. its methods include :-

  [ _25 May, 2022_ ]

  - `self.parallel(line)` : returns `True` if the given line is parallel to the current line.
  - `self.intersection(line)` : returns the intersection point of the current line and the given line.
  - `self.distance(other)` : returns the (shortest)distance between the current line and the given line or point.
  - `self.intersect(line)` returns `True` if given line intersects with the current line.
  - `self.includes` : returns `True` if the given point is on the current line.

  [ _26 May, 2022_ ]

  - To construct a line object instance :
    ```python
    # if p1 and p2 are points on the line
    line1 = vectogebra.geometry.line(p1, p2)
    # if a is a point on the line and b is the direction vector :
    line2 = vectogebra.geometry.line(point = a, direction = b)
    # in place of point, p or pt can also be used.
    # in place of direction, d or dir can also be used.
    ```
  - equality of line also defined : if two lines have same direction and one point in common, they are equal.
  - `line.__eq__(other)` : returns `True` if the given line is equal to the current line. else returns `False`.

    ```python
     >>>import vectogebra
     >>>line1 = vectgebra.geometry.line(p=vectogebra.vector(0,0,0),d=vectogebra.vector(1,1,1))
     >>>line2 = vectogebra.geometry.line(p=vectogebra.vector(5,5,5),d=vectogebra.vector(99,99,99))
     >>>line1 == line2
     >>>True
    ```

    [*27 May, 2022*]

  - defination of line can be done using tuples or strings also

    ```py
    import vectogebra.geometry as geo
    line1 = geo.line(p=(0,0,0),d=(1,1,1))
    # OR :
    line2 = geo.line(p='0 0 0',d='1 1 1')
    ```

  - Now line can also be constructed using `tuple` or `list` instead of `vector` :
    ```py
    line1 = vectogebra.geometry.line(p=(1,2,4),d=(15,12,33))
    # two point method also applicable :
    line2 = vectogebra.geometry.line((12,46,67),(12,98,65))
    # similarly, tuples can also be used.
    ```

- Class `plane` defined : Represents a plane in 3D space.

  [27 May, 2022]

  - different methods of defining the plane.
  - equality of planes.
  - intersection of plane with a line (result is a point.)
  - intersection of plane with a plane (result is a line)
  - function to check if a plane includes a given point or not.
  - function to check if a plane is parallel to a given plane or line.
  - distnce between a plane and a point or line or other plane.
  - now arguments need not be vectors, tuples/ lists / strings can also be used.

  ```py
  import vectogebra.geometry as geo
  plane1 = geo.plane(p=(0,0,0),n=(1,1,1))
  # OR
  plane2 = geo.plane(p='0 0 0',n='1 1 1')
  ```

### 3. changes in utilities.py mudule:

- `proportional(a,b)` function defined to check proportionality of two vectors.
- bug fixes
