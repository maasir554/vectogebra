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

### 2. changes in geometry.py mudule:

- `coplanar()` function defined. this function returns `True` if the given points are coplanar. else returns `False`. - _23 May, 2022_

- Class `line` defined. this class represents a line in 3-dimensional space. its methods inclode :-
  - `self.parallel(line)` : returns `True` if the given line is parallel to the current line.
  - `self.intersection(line)` : returns the intersection point of the current line and the given line.
  - `self.distance(other)` : returns the (shortest)distance between the current line and the given line or point.
  - `self.intersect(line)` returns `True` if given line intersects with the current line.
  - `self.includes` : returns `True` if the given point is on the current line.
