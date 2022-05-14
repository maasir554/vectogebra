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
     (radians)

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
4. `area_polygon` : signed area fo polygon with any number of vertices. 
5. `area_triangle` : area formed by a triangle with vertices `a` , `b` and `c`.
