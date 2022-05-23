# vectogebra v 0.0.7 - 15 May 2022

### Python module for vector algebra

easy to use vector algebra library for python, that lets ypu work with vectors in an efficient way.
apart from core vector object, many other vector operations are supported.
these can be imported from vectogebra.utilities.

this library was made by keeping its applications in Physics in mind (Mechanics, Optics, etc.)

- does not depend on any external libraries except math library.
- fully functional
- easy to use
- supports nearly all vector operations
- beginner friendly
- physics friendly
- Open for modifications

## 🌠 Install

```bash
pip install --upgrade vectogebra
```

### ⭐ Start by importing the vector class

```python
import vectogebra.vector as vect
```

_OR_

```python
from vectogebra import vector as vect
```

### ⭐ Also import useful utility functions

```python
import vectogebra.utitlies as vut
```

_OR_

```python
from vectogebra import utilities as vut
```

### ⭐ import functions for geometry applications :

```python
from vectogebra import geometry as geo
```

_OR_

```python
import vectogebra.geometry as geo
```

## 🧾 Description of the module

this module currently have two components : one is `vectogebra.vector`, which is the vector class (boject) defination. it contains the basic functionality.
the second component, `vectogebra.utilities` contains useful functions that are defined for the above mentioned vector class like, function to find angle between
two vectors, etc.

Create a vector object :

```python
import vectogebra.vector as vect

v1 = vect(1,2,3)
```

### 🔢 Algebric operations :

#### 1. Addition

consider two(or more) vectors : a,b,...
their sum will be given by :
`s = a + b + ...`
sum `s` will also be a vector object.

#### 2. Subtraction

Vectors can be subtracted using the minus (`-`) operator.

example :

`s = a - b + c - d + ...`

resultant `s` will also be a vector object.

#### 3. Dot product / scalar product and scalar multiplication

the `*` operator will be used for dot product, or multiplication by a scalar.

example :

`p = a * b * c * d * ...` is same as "a dot b dot c dot ...".

`p = 5*v` OR `v*5` is same as "scalar 5 multiplied to vector v".

#### 4. Cross product / vector multiplication

the `^` operator (XOR operator) will be used for cross product, or vector product.

example :

`p = a^b` is same as "p equals a cross b".

5. division by a scalar

simply divide a vector by a scalar.
NOTE : division by zero or division vector is not supported.

example :

`p = v / 5` is same as "p equals v divided by 5".

### ❌✔️ Logical operations :

#### 1. Equality

`a == b` returnes True when a and b are equal in magnitude and direction. else, it returns False

#### 2. Inequality

`a != b` have its usual meaning

#### 3. grater / lesser

the **magnitude** of the vectors can be compared using common logical operators.

```python
# a and b are vectors
a > b
a < b
a >= b
a <= b
```

## Attributes of the vector object

### Components

for a vector v1,

1. `v1.x` **OR** `v1.i`
2. `v1.y` **OR** `v1.j`
3. `v1.z` **OR** `v1.k`

### Magnitude

4. `v1.magnitude` **OR** `vi.mod`

### Magnitude squared (useful when precesion is required)

5.  `v1.magnitude_squared` **OR** `v1.mod_squared`

### Type

6. `v1.type` different from `type(v1)`

## 🚀 Vectogebra's Utitlies (vut)

important utility functions for the vector object.
**import** :

```python
import vectogebra.utilities as vut
```

| S. no. | function                                       | Return value                                                  |
| ------ | ---------------------------------------------- | ------------------------------------------------------------- |
| 1.     | `vut.angle(v1,v2)`                             | angle between v1 and v                                        |
| 2.     | `vut.dot(v1,v2)`                               | dot product (or scalar product) of vectors v1 and v2          |
| 3.     | `vut.cross(v1,v2)`                             | cross product (or vector product) of v1 and v2                |
| 4.     | `vut.magnitude(v1)`                            | magnitude of v1 and v2                                        |
| 5.     | `vut.is_perpendicular(v1,v2)`                  | True when v1 is **perpendicular** to v2 else it returns False |
| 6.     | `vut.is_parallel(v1,v2)`                       | True whe v1 is parallel to ve else False                      |
| 7.     | `vut.scalar_component_parallel(v1,v2)`         | _Magnitude_ of **component** of v1 **parallel** to v2         |
| 8.     | `vut.scalar_component_perpendicular(v1,v2)`    | _Magnitude_ of **component** of v1 **perpendicular** to v2    |
| 9.     | `vut.vector_component_parallel(v1,v2)`         | _Vector_ **component** of v1 **parallel** to v2               |
| 10.    | `vut.vector_component_perpendicular(v1,v2)`    | _Vector_ compoment of v1 perpendicular to v2                  |
| 11.    | `vut.unit_vector(v)` **OR** `vut.direction(v)` | Returns the **unit vector** parallel to v                     |
| 12.    | `vut.dot(v1,v2)`                               | **dot** product                                               |
| 13.    | `vut.cross(v1,v2)`                             | **cross** product                                             |
| 14.    | `vut.parallelogram_area(v1,v2)`                | parallelogram's area formed by joining v1 and v2 tail to tail |
| 15.    | `vut.box(a,b,c)`                               | Box product or scalar triple product                          |
| 16.    | `vut.collinear(a,b,c)`                         | returns True if a,b,c are collinear                           |
| ⭐     | **Conversions**                                |                                                               |
| 17.    | `vut.vector_to_list(v)`                        | a list of the components of v                                 |
| 18.    | `vut.vector_to_dict(v)`                        | a dictionary of the components of v                           |
| 19.    | `vut.vector_to_tuple(v)`                       | a tuple of the components of v                                |
| 20.    | `vut.list_to_vector(l)`                        | a vector object from a list of components                     |
| 21.    | `vut.dict_to_vector(d)`                        | a vector object from a dictionary of components               |
| 22.    | `vut.tuple_to_vector(t)`                       | a vector object from a tuple of components                    |

(more to come)

## 📈 Geometry related functions :

consider vectors `a`, `b` and `c` :

| S. no. | function                 | Return value                                                                                            | ⚠ Warning                                                      | 📃 Special instructions                                                |
| ------ | ------------------------ | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1.     | `divider(a,b,m,n)`       | a position vector of a point that divides the line segment joining `a` and `b` by in the ratio `m`:`n`. | atleast one of `m` or `n` must be non-zero                     |                                                                        |
| 2.     | `distance(a,b)`          | distance between `a` and `b`                                                                            |                                                                |                                                                        |
| 3.     | `area_line(a,b)`         | signed area under the line segment joining `a` and `b`.                                                 | x-y plane only (or area under projection of line on x-y plane) |                                                                        |
| 4.     | `area_polygon(*args)`    | Signed area of polygon whose vertices are given as input                                                | x-y plane only (or projection on x-y plane)                    | if vertices listed in cyclic manner the area will be +ve else -ve.     |
| 5.     | `area_triangle(a, b, c)` | Area of triangle with vertices `a` , `b`, and `c`                                                       |                                                                |                                                                        |
| 6.     | `coplanar(*args)`        | `True` : If all the points are coplanar else `False`                                                    | Arguments must be **position vectors.**                        | Keep in mind the difference between a _vector_ and a _position vector_ |

---

Author: Mohammad Maasir

License: MIT

date-created: 8th of May, 2022

PyPi :https://pypi.org/project/vectogebra/

---

_Copyright © 2022 Mohammad Maasir_
