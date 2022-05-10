# vectogebra v 0.0.6

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

---

Author: _Mohammad Maasir_

License: _MIT_

date-created: _8th of May, 2022_

---

# 💥 Install

`pip install vectogebra`

### ⭐ Start by importing the vector class

`import vectogebra.vector as vect`

_OR_

`from vectogebra import vector as vect`

### ⭐ Also import useful utility functions

`import vectogebra.utitlies as vut`

_OR_

`from vectogebra import utilities as vut`

---

# 🔥 Description of the module

## Create a vector object :

`v1 = vect(1,2,3)`

---

## 🔢 Algebric operations :

### 1. Addition

consider two(or more) vectors : a,b,...
their sum will be given by :
`s = a + b + ...`
sum `s` will also be a vector object.

### 2. Subctraction

Vectors can be subtracted using the minus (`-`) operator.

example :

`s = a - b + c - d + ...`

resultant `s` will also be a vector object.

### 3. Dot product / scalar product and scalar multiplication

the `*` operator will be used for dot product, or multiplication by a scalar.

example :

`p = a * b * c * d * ...` is same as "a dot b dot c dot ...".

`p = 5*v` is same as "scalar 5 multiplied to vector v".

### 4. Cross product / vector multiplication

the `^` operator will be used for cross product, or vector product.

example :

`p = a^b` is same as "p equals a cross b".

### 5. division by a scalar

simply divide a vector by a scalar.
NOTE : division by zero or division vector is not supported.

example :

`p = v / 5` is same as "p equals v divided by 5".

---

## ❌✔️ Logical operations :

---

### 1. Equality

`a == b` returnes True when a and b are equal in magnitude and direction. else, it returns False

### 2. Inequality

`a != b` have its usual meaning

### 3. grater / lesser

the **magnitude** of the vectors can be compared using common logical operators.

```
# a and b are vectors
a > b
a < b
a >= b
a <= b
```

---

## Attributes of the vector object

---

### Components

1. `v1.x` **OR** `vi.i`
2. `v1.y` **OR** `vi.j`
3. `v1.z` **OR** `vi.k`

### Magnitude

4. `v1.magnitude` **OR** `vi.mod`

### Magnitude squared (useful when precesion is required)

5.  `v1.magnitude_squared` **OR** `v1.mod_squared`

### Type

6. `v1.type` ==different from type(v1)==

---

## 🚀 Vectogebra's Utitlies (vut)

---

### 1. `vut.angle(v1,v2)`

### 2. `vut.dot(v1,v2)`

### 3. `vut.cross(v1,v2)`

### 4. `vut.magnitude(v1)`

### 5. `vut.unit(v1)`

### 6. `vut.is_perpendicular(v1,v2)`

### 7. `vut.is_parallel(v1,v2)`

### 8. `vut.scalar_component_parallel(v1,v2)`

### 9. `vut.scalar_component_perpendicular(v1,v2)`

### 10. `vut.vector_component_parallel(v1,v2)`

### 11. `vut.vector_component_perpendicular(v1,v2)`

### 12. `vut.unit_vector(v)` **OR** `vut.direction(v)` ==Returns the unit vector parallel to v==

### 13. `vut.dot(v1,v2)` ==dot product==

### 14. `vut.cross(v1,v2)` ==cross product==

### 15. `vut.parallelogram_area(v1,v2)` ==returns parallelogram area formed vy joining v1 and v2 tail to tail==

### 16. `vut.box(a,b,c)` ==Box product==

### 17. `vut.collinear(a,b,c)` ==returns true if a,b,c are collinear==

### 18. `vut.vector_to_list(v)` ==returns a list of the components of v==

### 19. `vut.vector_to_dict(v)` ==returns a dictionary of the components of v==

### 20. `vut.vector_to_tuple(v)` ==returns a tuple of the components of v==

### 21. `vut.list_to_vector(l)` ==returns a vector object from a list of components==

### 22. `vut.dict_to_vector(d)` ==returns a vector object from a dictionary of components==

### 23. `vut.tuple_to_vector(t)` ==returns a vector object from a tuple of components==

---

### ❤️ vectorogebra is open source and free to use.

---

_Copyright (c) 2022 Mohammad Maasir_
