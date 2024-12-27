# Python

References:
- [docs.python.org](https://docs.python.org/3/)
- [realpython.com](https://realpython.com/)
- [www.w3schools.com](https://www.w3schools.com/python/)

## Chapter 1. Variables, Literals, Objects, Types and Operators.

### Variables

**Notes**:
1. Python has no command for declaring a variable.
2. Python variables has no type belong.
3. 
4. Define a variables: `<var> = <value>`



```python
%reset -f
# Example
var = 1337
print("var   = ", var)
var = "Hello"
print("var   = ", var)

# More example
a, b, c = 1, 2, 3 # more detail this will be later
print("a b c = ", a, b, c)
x = y = z = "Hi" # more detail this will be later
print("x y z = ", x, y, z)
```

> **Note: Comment in Python**  
> In python, we to can use `# comment` for comment in one line or `""" comment """` for multiple line. Example:
> ```python
> # This is comment
> x = 1 # comment after statements
> """
> Multiline
> Comment
> """
> ```

> **Note: about Constants**  
> In python, we don't have constant variables. So, we cannot define it.
>

### Literals

See more about Python's literals [here](https://docs.python.org/3/reference/lexical_analysis.html#literals)

Literals are notations for constant values of some built-in types. Example: `x = 10`  
Some literals in python:
- String: `"this is string"`, `'this is string'`
- Multiline string: `"""string"""`, `'''string'''`
- Raw string: `r"string"`, `R"string"`, `r'string'`, `R'string'`, ...
- Formatted string (like string with `'f'` or `'F'` in prefix): `f'string'`, ...
- Bytes (like string with `'b'` or `'B'` in prefix): `b'bytes'`, ...
- Raw bytes (like string with `'rb'` or ... in prefix): `rb'bytes'`, ...

> **Note: Escape Sequences**  
> Escape sequences in python is similar to in C. Raw string or bytes will ignore all escape sequences in the literal. Some popular escape sequences: `'\n'`, `'\r'`, `'\xhh'`, ...  
> See more detail in [here](https://en.wikipedia.org/wiki/Escape_sequences_in_C#Escape_sequences)
>

> **Note: Prefix**  
> Bytes and string prefix can join with `'''`, `"""`, `"`, `'` to make more literals syntax. Example, multiline raw bytes: `rb'''bytes'''`
> 


```python
%reset -f
# Example string
s1 = "This is 'string'"
s2 = 'This is \'string\''
s3 = r'This is \'raw string\''
s4 = """
Multiple line:
- 1st
- 2nd
"""
s5 = "Just one \
line"
print(s1, s2, s3, s4, s5, sep='\n')
# f-string
print(f"String s1: {s1}")
```

    This is 'string'
    This is 'string'
    This is \'raw string\'
    
    Multiple line:
    - 1st
    - 2nd
    
    Just one line
    String s1: This is 'string'
    


```python
%reset -f
# Example bytes
b1 = b'\xfe\xf1\x12\x45\x81\x65'
b2 = rb'\xfe\xf1\x12\x45\x81\x65'
print("Bytes    : ", b1)
print("Raw bytes: ", b2)
```


```python
%reset -f
# Formatted string
val = 3.1415
print(f"formatted: {val = }")
```

- Integer: `101`, `0xAe1`, `0b101`, `0o101`, `1_124_199`
- Floating-point: `3.14`, `10.`, `.12E0`, `271e-2`, `3.14_15`
- Imaginary: `10.j`, `3.14j`, `1j`
- Tuple: `(1, 2)`
- List: `[1, 2]`
- Dictionary: `{'key': 'value'}`
- Set: `{1, 2, 3}`
- Boolean: `True`, `False`
- Ellipsis: `...`
- Special: `None`

### Objects

**Objects** are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. Every object has an identity, a type and a value.  

- **Mutable objects** is objects whose value can change.
- **Immutable objects** is objects whose value is unchangeable once they are created.

> **Note**:
> - Variables in python just contain a reference to a objects not a objects. Unlike in java, variables can contain both a reference to a objects or a objects.
> - We can use `id()` function to get id of an object which identify it with others.
> - Objects are never explicitly destroyed; however, when they become unreachable they may be garbage-collected.
> - For immutable types, operations that compute new values may actually return a reference to any existing object with the same type and value, while for mutable objects this is not allowed.



```python
%reset -f
# Example on int object.
int_x = 1
int_y = 1
print(f"{id(int_x) = }")
print(f"{id(int_y) = }")
print(f"{(int_x == int_y) = }")
```


```python
%reset -f
# Example on float object.
float_x = 1.
float_y = 1.
print(f"{id(float_x) = }")
print(f"{id(float_y) = }")
print(f"{(float_x == float_y) = }")

float_z = float_y = 1.
print(f"{id(float_y) = }")
print(f"{id(float_z) = }")
```


```python
%reset -f
# Example on list object
list_x = []
list_y = []
print(f"{id(list_x) = }")
print(f"{id(list_y) = }")
print(f"{(list_x == list_y) = }")

list_z = list_y = []
print(f"{id(list_y) = }")
print(f"{id(list_z) = }")
```


```python
# List is multable
list_y.append(0)
print(f"{id(list_y) = }")
print(f"{list_y = }")
print(f"{list_z = }")
```

> **Note**:
> We cannot not copy a list by assignment like `list_a = list_b`. Some way to copy:
> - Loop throw two list and assign each element.
> - Use `copy` module.
> Detail above will learn later.

**Summary about example**  
&emsp;![Figure1](Figure1.jpg)

### Types

Python types tree:
- **NoneType**: This type has a single value. There is a single object with this value. This object is accessed through the built-in name `None`. Its truth value is false.
- **NotImplementedType**: This type has a single value. There is a single object with this value. This object is accessed through the built-in name `NotImplemented`. It should not be evaluated in a boolean context.
- **Ellipsis**: This type has a single value. There is a single object with this value. This object is accessed through the literal `...` or the built-in name `Ellipsis`. Its truth value is true.
- **numbers.Number**: These are created by numeric literals. Numeric objects are immutable.
  - **numbers.Integral**: These represent elements from the mathematical set of integers (positive and negative).
    - **int**: These represent numbers in an unlimited range.
    - **bool**: These represent the truth values False and True.
  - **float**: These represent machine-level double precision floating-point numbers.
  - **complex**: These represent complex numbers as a pair of machine-level double precision floating-point numbers.  
- **Sequences**: These represent finite ordered sets indexed by non-negative numbers. Support indexing and slicing.
  - **Immutable sequences**: An object of an immutable sequence type cannot change once it is created.
    - **str**: A string is a sequence of values that represent Unicode code points.
    - **tuple**: The items of a tuple are arbitrary Python objects.
    - **bytes**: The items are 8-bit bytes.
  - **Mutable sequences**: Mutable sequences can be changed after they are created.
    - **list**: The items of a list are arbitrary Python objects.
    - **bytearray**: A bytearray object is a mutable array.
- **Set types**: These represent unordered, finite sets of unique objects.
  - **set**: These represent a mutable set.
  - **frozenset**: These represent an immutable set.
- **Mappings**: These represent finite sets of objects indexed by arbitrary index sets.
  - **dict**: These represent finite sets of objects indexed by nearly arbitrary values.
- **Callable types**: These are the types to which the function call operation can be applied.
  - **function**: created by a function definition.

See more about Python's [the standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)  
See more about Python's [built-in types](https://docs.python.org/3/library/stdtypes.html)


```python
%reset -f
# Check type of some object
print(f"{type(None) = }")
print(f"{type(NotImplemented) = }")
print(f"{type(...) = }")
```


```python
# type of number objects
print(f"{type(1) = }")
print(f"{type(True) = }")
print(f"{type(1.) = }")
print(f"{type(1j) = }")
```


```python
# type of sequence objects
print(f"{type("Hello") = }")
print(f"{type((1, 2)) = }")
print(f"{type(b"Hi") = }")
print(f"{type([1, 2]) = }")
print(f"{type(bytearray([1, 2])) = }") # not have literals
```


```python
# type of set objects
print(f"{type({1, 2}) = }")
print(f"{type(frozenset([1, 2])) = }") # not have literals
```


```python
# type of dictionary objects and some other.
def f():
    pass
print(f"{type({}) = }")
print(f"{type(f) = }")
print(f"{type(print) = }")
```

> **Note**:  
> `{}` literal is a empty dictionary not a empty set. To create empty set use set constructor `set()`.

### Operators

**Notes**:  
1. Python operators work depend on types of operands.
2. Python is a strong typed language. So no implicit type conversion in python.

#### Operator with number types (int, float, bool, complex)

**Arithmetic operators**
| Operator | Name | Type of operand |
| :---: | :---: | :--: |
| `+` | positive | int, float, bool, complex |
| `-` | negative | int, float, bool, complex |
| `+` | Addition | int, float, bool, complex |
| `-` | Subtraction | int, float, bool, complex |
| `*` | Multiplication | int, float, bool, complex |
| `/` | Division | int, float, bool, complex |
| `**` | Exponentiation | int, float, bool, complex |
| `//` | Floor division | int, float, bool |
| `%` | Modulus | int, float, bool |

> **Note**:
> - All of above operator except `**` will make expression is valuated from left to right.
> - With `**` operator, expression `2**3**0` is equal to `2` not `1`.


```python
%reset -f
# Example

print(f"{12.4 + True = }")
print(f"{2j - False = }")
print(f"{3j / (1 - 2j) = }")
print(f"{-9.8j * False = }")

print(f"{2j ** 1j = }")

print(f"{3.14 // 1.5 = }")
print(f"{3.14 % 2.1 = }")
print(f"{2.71 % True = }")
```


**Number comparison operators**
| Operator | Name | Type of operand |
| :---: | :---: | :--: |
| `==` | Equal | int, float, bool, complex |
| `!=` | Not equal | int, float, bool, complex |
| `>` | Greater | int, float, bool |
| `<` | Less| int, float, bool |
| `>=` | Greater or Equal | int, float, bool |
| `<=` | Less or Equal | int, float, bool |

> **Note**:
> - Number comparison in python has more mathematic significant than some other language. Example, in JS `4 > 3 > 2` = `(4 > 3) > 2` = `True > 2` = `False`. But in python, `4 > 3 > 2` = `True` and `(4 > 3) > 2` = `False`.


```python
print(f"{(False == 0. + 0.j) = }")
print(f"{(True != 1) = }")
print(f"({(True < 2) = }")
print(f"{(False > 0) = }")
```

    (False == 0. + 0.j) = True
    (True != 1) = False
    ((True < 2) = True
    (False > 0) = False
    

**Bitwise operators**
| Operator | Name | Type of operand |
| :---: | :---: | :--: |
| `&` | and | int, bool |
| `\|` | or | int, bool |
| `^` | xor | int, bool |
| `~` | not | int, bool |
| `<<` | left shift | int, bool |
| `>>` | right shift | int, bool |

> **Notes**:
> 1. Negative shift counts are illegal.
> 2. The result of bitwise operations is calculated as though carried out in two’s complement with an infinite number of sign bits.



```python
# Some interesting example
print(f"{~True = }")
print(f"{~False = }")
print(f"{-1 >> 10 = }")

```

    ~True = -2
    ~False = -1
    -1 >> 10 = -1
    

#### Other operator in various types.

**Boolean Operators**
| Operator | Result |
| :---: | :---: |
| `x or y` | if x is true, then x, else y |
| `x and y` | if x is false, then x, else y |
| `not x` | if x is false, then `True`, else `False`|

> **Notes**:
> 1.  The Boolean operations `or` and `and` always return one of their operands.
> 2.  `or` and `and` is a short-circuit operator.
> 3.  `not` has a lower priority than non-Boolean operators.

> **Note: Truth Value Testing**
> - Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations.
> - Carefully, Truth Value is not boolean object.
> - By default, an object is considered true. Here are most of the built-in objects considered false:
>   - constants defined to be false: `None` and `False`
>   - zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
>   - empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`


```python
%reset -f
#Example
x = 10 # true
y = [] # false
z = 0j # false

print(f"{x = }")
print(f"{y = }")
print(f"{(x is True) = }")
print(f"{(y is not False) = }")
print(f"{(y and x) = }")
print(f"{(x or y) = }")
print(f"{z = }")
print(f"{(z or y) = }")
print(f"{(not y) = }")
```

    x = 10
    y = []
    (x is True) = False
    (y is not False) = True
    (y and x) = []
    (x or y) = 10
    z = 0j
    (z or y) = []
    (not y) = True
    


```python
%reset -f
#Example
x = 10 # true
y = [] # false
z = 0j # false

print(f"{y.append(0) = }, {y = }")
print(f"{(x or y.append(0)) = }, {y = }")
print(f"{(z or y.append(0)) = }, {y = }")
```

    y.append(0) = None, y = [0]
    (x or y.append(0)) = 10, y = [0]
    (z or y.append(0)) = None, y = [0, 0]
    

**More comparision operator**
| Operator | Meaning |
| :---: | :---: |
| `is` | object identity |
| `is not` | negated object identity |

> **Notes**:
> 1. `is not` is a operator, isn't combine between `is` and `not` operator. Example above, `y is not False` isn't `y is True`.
> 2. Above operator will compare id of operand objects.



```python
%reset -f
# Example
float_x = 1.
float_y = 1.
int_x = 1
int_y = 1
var = []

print(f"{(float_x is float_y) = }\n{(float_x == float_y) = }")
print(f"{(int_x is int_y) = }\n{(int_x == int_y) = }")

print(f"{(var is not False) = }")
print(f"{(var is     True ) = }")
```

    (float_x is float_y) = False
    (float_x == float_y) = True
    (int_x is int_y) = True
    (int_x == int_y) = True
    (var is not False) = True
    (var is     True ) = False
    

**Assignment Operators**
| type assigment | operator | 
| :---: | :---: |
| Assigment | `=` |
| Compound assigment | `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `&=`, `\|=`, `^=`, `<<=`, `>>=` |
| Walrus | `:=` |


```python
%reset -f
# Walrus example
x = (y := 1) + 1
print(f"{x = }, {y = }")
```

    x = 2, y = 1
    

**Membership Operators**
| Operator | Meaning |
| :---: | :---: |
| `in` | `True` if an item of s is equal to x, else False |
| `not in` | False if an item of s is equal to x, else True |


```python
%reset -f
# Example
arr = [1, 2, 3]
print(f"{arr = }")
print(f"{0 in arr = }")
print(f"{1 in arr = }")

```

    arr = [1, 2, 3]
    0 in arr = False
    1 in arr = True
    

**@ operator**  
In some library, operator `@` is also used. Example in `numpy`, `@` operator is used as matrix multiplication operator.

#### Operator precedence

| Operator |
| :---: |
| `()` |
| `**` |
| `+x`, `-x`, `~x` |
| `@`, `*`, `/`, `//`, `%` |
| `+`, `-` |
| `<<`, `>>` |
| `&` |
| `^` |
| `\|` |
| `==`, `!=`, `>`, `<`, `<=`, `>=`, `is`, `is not`, `in`, `not in` |
| `not` |
| `and` |
| `or` |
| `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `&=`, `\|=`, `^=`, `<<=`, `>>=`, `:=` |

For more detail about operators and expression, check [here](https://docs.python.org/3/reference/expressions.html)



```python

```
