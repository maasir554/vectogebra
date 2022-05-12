# CHANGELOG

record of major changes to the project including bug fixes will be stored here.

## [0.0.6]

### the library is now comlpetely functional.

- optimised the directory structure.
- importing vector class is now easy.
- resolved the issue of angle between parallel vectors.

## [0.0.7]

### updates in vector class

- 2D vector can now be defined by passing two arguments and third woll automatically be set to 0.
- vector() can now accept single argument as a list / dict or tuple of x, y, and z components.

### updates in vut

- polar vectors are now supported.
  to define a vector using polar argument, use vut.polar_to_vector(r, theta, atype)
  atype can be 'deg' / 'degree' or 'rad' / 'radian' default is 'deg'. example:
  ```python
    >>> vut.polar_to_vector(1, 90, 'deg')
    >>> vut.polar_to_vector(1, math.pi/2, 'rad')
  ```
