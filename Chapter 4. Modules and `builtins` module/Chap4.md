# Python

References:
- [docs.python.org](https://docs.python.org/3/)
- [realpython.com](https://realpython.com/)
- [www.w3schools.com](https://www.w3schools.com/python/)

## Chap 4. Modules and `builtins` module

- Creating a **script**.
- Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a **module**.
- Definitions from a module can be *imported* into other modules or into the *main* module.
- A module is a file containing Python definitions and statements. The file name is the module name with the suffix *.py* appended.
- Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.

### Modules

#### Using module

**Import a module**  
**Syntax:** `import <module> [as <alias>] [, <module> [as <alias>] ...]`

- Each module has its own private **namespace**, which is used as the **global namespace** by all functions defined in the module.
- To use a item in *imported module* use `<module>.<items>` (item maybe is classes, variables, functions in *imported* module).
- Modules can import other modules. It is not required to place all import statements at the beginning of a module.
  


```python
%reset -f
import nbtool

print(type(nbtool))
nt = nbtool
print(f"{nt.__name__ = }")
print(f"{nt.gcd(12, 28) = }")
print(f"{nt.lcm(12, 28) = }")

print(f"{__name__ = }")
```

*A module can contain executable statements:*


```python
%reset -f
import exmod

```


**Import a part of module**  
**Syntax:** `from <module> import <item> [as <alias>] [, <item> [as <alias>] ...]`

> **Note**:
> To import all use `from <module> import *`. This imports all names except those beginning with an underscore (_).


```python
%reset -f
from nbtool import legendre as l

print(dir())
print(f"{l(8, 17) = }")

```


#### `if __name__ == "__main__"`

Use write test code for a module but don't not run it when `import`.

#### The Module Search Path

1. The interpreter first searches for a built-in module with that name.
2. If not found, it then searches for a file named spam.py in a list of directories given by the variable `sys.path`:
   - The directory containing the input script
   - `PYTHONPATH`
   - The installation-dependent default.

> **Notes:**
> Python has many standard library for various purpose called **Standard Modules**. You can see more about them in [The Python Standard Library](https://docs.python.org/3/library/index.html) page.

### Packages

#### What is Packages?

- Packages are a way of structuring Python’s module namespace by using “dotted module names”.
- When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.
- The `__init__.py` files are required to make Python treat directories containing the file as packages.

**Example:** package struct.
```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

#### Using Module in Package

**Syntax:** `import <package>[.<subpackage>...].<module>`

- it's same as `import` module above.
**Example:**
```python
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
```

**Notes:**
- When using syntax like `import item.subitem.subsubitem`, each item except for the last must be a package.
- The last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

#### Importing * From a Package

- if a package’s `__init__.py` code defines a list named `__all__`, it is taken to be the list of module names that should be imported when `from package import *` is encountered.
- If `__all__` is not defined, it only ensures that the `package` has been imported and then imports whatever names are defined in the package.

#### Intra-package References

**Example:**
- `from . import <module\package>`  import in same package.
- `from .. import <module\package>` import in same parent of parent package.

> See more about module and package [here](https://docs.python.org/3/tutorial/modules.html).

### `builtins` module

Python provides for user built-in types, constants, exceptions and functions. To use them, we not need to `from builtins import *`, it's default in python (python find these in `builtins` namespace, through `__builtins__` variable)

#### Built-in Types

We learned many about Python's buitins types but not all. For more about type, check [here](https://docs.python.org/3/library/stdtypes.html).

#### Built-in Constants

Some built-in constant:
- `False`
- `True`
- `None`
- `NotImplemented`
- `Ellipsis`

For detail in these constants check [here](https://docs.python.org/3/library/constants.html).

#### Built-in Exceptions

(Not need learn)
- If want to read about this topic, check [here](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).
- About exception we will learn later.

#### Built-in Functions

For all built-in functions (there are 68 functions), check [here](https://docs.python.org/3/library/functions.html).

Some learned (enough) built-in function:
- `bool()`
- `complex()`
- `dict()`
- `enumerate()`
- `float()`
- `frozenset()`
- `id()`
- `int()`
- `list()`
- `reserved()`
- `set()`
- `str()`
- `tuple()`
- `type()`
- `range()`

##### For math

- `abs(x)` (obj.__abs__())
- `divmod(a, b)`
- `pow(base, exp, mod=None)` (!)
- `round(number, ndigits=None)`



```python
%reset -f
# Example

print(f"{abs(-1.5) = }")
print(f"{abs(3+4j) = }")

print(f"{divmod(9   , 2) = }")
print(f"{divmod(3.14, 1) = }")

print(f"{pow(-9, 0.5) = }")
print(f"{pow(2, 9, 7) = }")
print(f"{pow(2,-1, 7) = }")

print(f"{round( 0.5) = }")
print(f"{round(-0.5) = }")
print(f"{round( 1.5) = }")
print(f"{round(2.675, 2) = }")
```


**all/any**

- `all(iterable)`
- `any(iterable)`



```python
%reset -f
# Example

l = [1, 0, 0, 0, 1, 1, 1]
print(f"{all(l) = }")
print(f"{any(l) = }")

print(f"{all([]) = }")
print(f"{any([]) = }")

```


**For IO**

- `print(*objects, sep=' ', end='\n', file=None, flush=False)`
- `input()`
- `input(prompt)`



```python
%reset -f
# Example

print("How", "are", "you?")
ans = input("Answer: ")
print(ans)

```


**For changing base**

- `hex(x)`
- `bin(x)`
- `oct(x)`
(__index__())



```python
%reset -f
# Example

n = 1000
print(f"{bin(n) = }")
print(f"{oct(n) = }")
print(f"{hex(n) = }")

```


**Charcode**

- `ord(c)`
- `chr(i)`



```python
%reset -f
# Example

print(f"{ord('€') = }")
print(f"{chr(8364) = }")

```


**For statistics**

- `max(iterable, *, key=None)`
- `max(iterable, *, default, key=None)`
- `max(arg1, arg2, *args, key=None)`
- `min(iterable, *, key=None)`
- `min(iterable, *, default, key=None)`
- `min(arg1, arg2, *args, key=None)`
- `sum(iterable, /, start=0)`
- `len(s)`



```python
%reset -f
# Example

l = [1, 2, -5, 7, 9, -17, 13, 0, 2, -1, 14]

print(f"{min(l) = }")
print(f"{max(l, key=(lambda x: x**2)) = }")
print(f"{sum(l, start=-100) = }")

```


**For bytes**

- `bytes(source=b'')`
- `bytes(source, encoding)`
- `bytes(source, encoding, errors)`
- `bytearray(source=b'')`
- `bytearray(source, encoding)`
- `bytearray(source, encoding, errors)`



```python
%reset -f
# Example

b1 = bytes(10)
b2 = bytes("Hello", encoding="utf-8")
ba = bytearray([123, 12, 65, 107])

print(f"{b1 = }")
print(f"{b2 = }")
print(f"{ba = }")

```


**map/filter**

- `map(function, iterable, *iterables)`
- `filter(function, iterable)`



```python
%reset -f
# Example

l1 = [1, 3, 5, 7]
l2 = [1, 2, 5, 6]
l3 = [-1, 1, 1, -1]

lm = list(map(lambda x1, x2, x3: (x1 + x2)*x3, l1, l2, l3))
lf = list(filter(lambda x: x > 0, lm))

print(f"{lm = }")
print(f"{lf = }")
```


**eval/exec**

- `eval(source, /, globals=None, locals=None)`
  - **source** (*str* | *code object*) – A Python expression.
  - **globals** (*dict* | `None`) – The global namespace.
  - **locals** (*mapping* | `None`) – The local namespace.
- `exec(source, /, globals=None, locals=None, *, closure=None)`



```python
%reset -f

# Example for exec
code = """
# global greet
def greet(name):
    return f'Hello, {name}!'
print(f"{list(locals()) = }")
print(f"{list(globals())= }")
print(f"{type(__builtins__) = }")
"""
# exec(code, None, {})
exec(code)
print(greet("Alice"))

# Example for eval
expression = "3 * (4 + 5)"
result = eval(expression)
print(f"The result of the expression '{expression}' is: {result}")
```


**dir**

- `dir()`
- `dir(object)`
(__dir()__)

*Return:*
- Without arguments, return the list of names in the current local scope.
- If the object is a module object, the list contains the names of the module’s attributes or find out which names a module defines.
- If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.
- The list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.



```python
%reset -f
# Example

items = []
print(f"{dir() = }")

import nbtool as nt
print(f"{dir() = }")
print(f"{dir(nt) = }")

print(f"{dir(None) = }")
```
