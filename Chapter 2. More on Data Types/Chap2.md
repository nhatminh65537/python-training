# Python

References:
- [docs.python.org](https://docs.python.org/3/)
- [realpython.com](https://realpython.com/)
- [www.w3schools.com](https://www.w3schools.com/python/)

## Chap 2. More on data types.

**Review**:
- Object of a data types can create by literals or by constructor.

### Numbers

#### Numbers constructors

(this define as builtin function)
- Integer: `int(number=0, /)`, `int(string, /, base=10)`. More detail [here](https://docs.python.org/3/library/functions.html#int)
- Boolean: `bool(object=False, /)`. More detail [here](https://docs.python.org/3/library/functions.html#bool)
- Float: `float(number=0.0, /)`, `float(string, /)`. More detail [here](https://docs.python.org/3/library/functions.html#float)
- Complex: `complex(number=0, /)`, `complex(string, /)`, `complex(real=0, imag=0)`. More detail [here](https://docs.python.org/3/library/functions.html#complex).



```python
%reset -f
# Example use of constructor
i = int("1001", 2) # same as `i = 0b1001`
f = float("1.234")
b = bool(i)
c = complex(18, 20)
print(f"{i = }")
print(f"{f = }")
print(f"{b = }")
print(f"{c = }")

```

#### Some method and attribute on numbers

- `complex.imag`
- `complex.real`
- `int.bit_length()`
- `int.bit_count()`
- `int.to_bytes(length=1, byteorder='big', *, signed=False)`
- `classmethod int.from_bytes(bytes, byteorder='big', *, signed=False)`

> **Note**:
> - To check more method and attribute of object. Use `dir()` function.
> - See more about these types [here](https://docs.python.org/3/library/stdtypes.html#typesnumeric)


```python
%reset -f
# Example
z = 10 - 20j
print(f"{z.real = }, {z.imag = }")

print(f"{(0b10001).bit_count()  = }")
print(f"{(0b10001).bit_length() = }")

b = b"\xff\x00"
print(f"{int.from_bytes(b, signed=True) = }")
print(f"{(255).to_bytes(2, "little")    = }")
```


### String

#### String constructor

`class str(object='')`  
`class str(object=b'', encoding='utf-8', errors='strict')`

> To convert object to string, `str()` will involk method `obj.__str__()` of `obj` which return string prestation of `obj`. (Like in java, we have `toString()` method.



```python
%reset -f
# Example
print(f"{str(b'\x65') = }")
print(f"{str(b'\x65', 'utf-8') = }")
```


#### Some useful String Method

`str.encode(encoding='utf-8', errors='strict')`  
`str.split(sep=None, maxsplit=-1)`  
`str.strip([chars])`  
`str.zfill(width)`  
`str.lower()`  
`str.find(sub[, start[, end]])`  
`str.upper()`  
`str.join(iterable)`

See more string's method [here](https://docs.python.org/3/library/stdtypes.html#string-methods)


```python
%reset -f
# Example
s = " Hello World "

print(f"{s.encode() = }")
print(f"{s.split() = }")
print(f"{s.strip() = }")
print(f"{s.zfill(20) = }")
print(f"{s.lower() = }")
print(f"{s.upper() = }")
print(f"{s.find("World") = }")
print(f"{", ".join(s) = }")
```

#### Indexing and Slicing

Give string: `s = "Python"`

```python
 +---+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+---+
   0   1   2   3   4   5   6
  -6  -5  -4  -3  -2  -1
```

**Indexing**:  
- Get element has index i: `s[i]`. If index out of range, exception will be raised. Example: `s[5]`, `s[-1]`.
- Because string is immutable object, so this statement is wrong `s[-1] = 'N'`  


**Slicing**:  
- Get a substring from index i to before index j: `s[i: j]`. Example: `s[0: 1]`.
- Get a substring with step k: `s[i: j: k]`
- k default by 1.
- if (i - j)*k > 0, slice string will be empty.  
```python
       i                       j     (k > 0)
 +---+---+---+---+---+---+---+---+------------
 |   | P | y | t | h | o | n |   |
 +---+---+---+---+---+---+---+---+------------
   j                       i         (k < 0)
```

> **Tips**:
> - To get reversed string use `s[::-1]`
 


```python
%reset -f
# Example

s = "Python"
print(f"{s[ 0] = }")
print(f"{s[-1] = }")

print(f"{s[:]    = }")
print(f"{s[::-1] = }")
print(f"{s[:5:4] = }")
print(f"{s[:0:-4]= }")
```


#### Operations on string

Get string len: `len(s)`  
Concatenate:
- use operator `+`: `s1 + s2`
- concatenate two string literals: `"Hello" "World"`

Multiple string with operator `*`.  
Check substring in string with `in` and `not in`.



```python
%reset -f
# Example
s1 = "Hi"
s2 = "!"

print(f"{s1*3 + s2*2 = }")
print("Hello "
      "World!")
print("How" in "How are you")
```


#### Format String

There are several way to print a formatted string:
- Operater `%` (detail [here](https://docs.python.org/3/library/stdtypes.html#old-string-formatting))
- `str.format()` method (detail [here](https://docs.python.org/3/library/string.html#formatstrings))
- f-string (detail [here](https://docs.python.org/3/reference/lexical_analysis.html#f-strings))



```python
%reset -f
# Example

# str.format()
print("{} {} {} {three} {four} {three}".format("rei", "ichi", "ni", three = "san", four = "yon"))
print("{0} {1} {0} {three} {2} {four}".format("rei", "ichi", "ni", three = "san", four = "yon"))

# % operator
print('%s has %d quote types.' % ('Python', 2))
print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})

# f-string
number = 1024
print(f"{number = :#0x}")
print(f"{number = :#0b}")
```


### Lists

#### List constructor

`class list([iterable])`



```python
%reset -f
# Example: create lists

l1 = [1, 2, 3, 4]
l2 = list("abcd")

print(f"{l1 = }")
print(f"{l2 = }")

print(f"Empty list {list()}")
```


#### List Indexing and Slicing

- List indexing and slicing like string (they are sequence types).
- List is multable, so we can change list element value like `l[i] = val` or `l[i: j] = iterable`.

#### List method

There are some popular list method:
- `list.append(x)`
- `list.extend(iterable)`
- `list.insert(i, x)`
- `list.remove(x)`
- `list.pop([i])`
- `list.clear()`
- `list.index(x[, start[, end]])`
- `list.count(x)`
- `list.sort(*, key=None, reverse=False)`
- `list.reverse()`
- `list.copy()`

> **Other way to insert to a list**:
> - `a[len(a):] = iterable`
> - `a[len(a):] = [x]`
> 


```python
%reset -f
# Example
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(f"{fruits = }")
print(f"{fruits.count('apple') = }")
print(f"{fruits.index('banana') = }") # Raise exception if not found

fruits.reverse()
print(f"{fruits = }")

fruits.append('grape')
fruits.sort()
print(f"{fruits = }")

print(f"{fruits.pop() = }")
```


#### Operations on list

- Get list len: `len(l)`  
- Concatenate use operator `+`: `l1 + l2`
- Multiple list with operator `*`.  
- Check element in list with `in` and `not in`.
- Remove element in list with `del`



```python
%reset -f
# Example

l_int = [1, 2, 3]
l_str = ['a', 'b', 'c']

l = 2*l_int + l_str
print(f"{l = }, {len(l) = }")
print(f"{2 in l = }")

del l[:3]
print(f"{l = }")
```


#### Copy a list

Consider example:


```python
%reset -f
# Example
lists = [[]] * 3
print(f"{lists = }") 

lists[0].append(3)
print(f"{lists = }") 

```

Some way to copy a list:
- `l.copy()`.
- `copy.copy()` in `copy` module.
- `l[:]`
- `list(l)`

These above copy return a **shallow copy** of a list. There also have **deep copy**, but we consider later.



```python
%reset -f
# Example

l1 = [1, 2, 3]
l2 = [2, 3, 4]
l3 = [3, 4, 5]
lx = [l1, l2, l3]
ly = lx[:]

del lx[-1]
print(f"{lx = }")
print(f"{ly = }")

ly[-1][-1] = 100
ly[ 0][-1] = 100
print(f"{lx = }")
print(f"{ly = }")
```


#### List Comprehensions

(Learn later)

### Tuple

Tuple is like list but it's immutable.

#### Create Tuple

- By constructor: `tuple([iterable])`
- By literals: `t = 1,`



```python
%reset -f
# Example

t1 = tuple("abc")
t2 = (1, 2, 3)
t3 = [1, 2],

print(f"{t1 = }")
print(f"{t2 = }")
print(f"{t3 = }")

```

#### Tuple Method

`tuple.index()`
`tuple.count()`

#### Tuple indexing and slicing

- Tuple indexing and slicing like list.
- Tuple is immultable, so we cannot change tuple element value like `t[i] = val` or `t[i: j] = iterable`.

#### Operations on tuple

- Get tuple len: `len(t)`  
- Concatenate use operator `+`: `t1 + t2`
- Multiple tuple with operator `*`.  
- Check element in tuple with `in` and `not in`.

### Set and Frozenset

#### Construct

- `set([iterable])`
- `frozenset([iterable])`

> Frozenset is set with immutable property.



```python
%reset -f
# Example

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a = set('abracadabra')
b = set('alacazam')

print(f"{a = }")
print(f"{b = }")

```

#### Method

- `set.isdisjoint(other)`
- `set.issubset(other)`
- `set.issuperset(other)`
- `set.union(*others)`
- `set.intersection(*others)`
- `set.difference(*others)`
- `set.symmetric_difference(other)`
- `set.copy()`
- `set.update(*others)`
- `set.intersection_update(*others)`
- `set.difference_update(*others)`
- `set.symmetric_difference_update(other)`
- `set.add(elem)`
- `set.remove(elem)`
- `set.discard(elem)`
- `set.pop()`
- `set.clear()`

#### Operators

- Get len of set: `len(s)`
- Check subset and superset: `<=`, `<`, `>=`, `>`
- Union, intersetion, difference, symmetric_difference: `|`, `&`, `-`, `^`
- Update: `|=`, `&=`, `-=`, `^=`


```python
print(f"{a = }")
print(f"{b = }")

u = a | b
i = a & b
d = a - b
x = a ^ b
print(f"{u = }")
print(f"{i = }")
print(f"{d = }")
print(f"{x = }")

print(f"{x < u = }")
```


#### Set Somprehension

(Learn later)

### Dictionary

#### Create Dictionary

**Constructor**:
- `dict(**kwargs)`
- `dict(mapping, **kwargs)`
- `dict(iterable, **kwargs)`



```python
%reset -f
# Example
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)

print(a)
print(a == b == c == d == e == f)
```


#### Dictionary operations

- `list(d)`
- `len(d)`
- `d[key]`
- `d[key] = value`
- `del d[key]`
- `key in d`
- `key not in d`
- `d | other`
- `d |= other`

> **More**:
> - To get dictionary keys: `list(d.keys())`
> - To get dictionary values: `list(d.values())`
> - To get dictionary items: `list(d.items())`
>
> For more about dictionary see [here](https://docs.python.org/3/library/stdtypes.html#typesmapping).
> 


```python
# Example

print(f"{a = }")
a["four"] = 4
del a["one"]
a |= {"ten": 10, "nine": 9}
print(f"{a = }")

```

#### Dict Comprehensions

Learn later.

### Range


The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed).

**Create range**:
- `range(stop)`  
- `range(start, stop[, step])`

**Operation on range**:
- Slicing
- Indexing
- Member test


```python
%reset -f
# Example
r = range(0, 30, 5)

print(f"{r = }")
print(f"{1 in r = }")
print(f"{5 in r = }")
print(f"{r[4] = }")
print(f"{r[1: 4] = }")
print(f"{list(r) = }")

```


### Sequence types

#### Sequences packing and unpacking

Packing:
- Tuple packing: `t = 1, 2, 3`

Unpacking:
- Tuple unpacking: `a, b, c = t`
- List unpacking: `a, b, c = l`
- Unpacking with starred expression: `a, *b = t`

> Note that multiple assignment is really just a combination of tuple packing and sequence unpacking. 


```python
%reset -f
# Example

t = 1, 2, 3, 4, 5 # tuple packing
print(f"{t = }")
```


```python
a, *b, c = t # tuple unpacking
print(f"{a = }, {b = }, {c = }")
```


```python
x, y, z = b # list unpacking
print(f"{x = }, {y = }, {z = }")
```


#### Comparision in sequence types.

- Ordered sequence types: list, str, tuple, range.
- The comparison uses lexicographical ordering.

Example:
```
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
