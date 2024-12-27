# Python

References:
- [docs.python.org](https://docs.python.org/3/)
- [realpython.com](https://realpython.com/)
- [www.w3schools.com](https://www.w3schools.com/python/)

## Chap 3. Flow Control and Function

### `if` Statement

**Syntax:**  
```python
if <condition>:
    <statement>
    ...
[elif <condition>:
    <statement>
    ...
...]
[else:
    <statement>]
```

> **Tips:** We can use `if` statement as ternary `?:` in other language.  
> **Syntax:** `<expression> if <condition> else <expression>`


```python
%reset -f
# Example

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

print(("Less" if x < 100 else "Greater") + " than 100")
```


### `while` Statement

**Syntax:**
```python
while <condition>:
    <statment>
    ...
```



```python
%reset -f
# Example

a, b = 0, 1
while a < 100000:
    print(a, end=', ')
    a, b = b, a+b

```


### `for` Statement

**Syntax:**
```python
for <var_list> in <iterable object>:
    <statement>
    ...



```python
%reset -f
# Example on list

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```


```python
%reset -f
# Example on dictionary

animals = dict(cat=100, dog=115, chicken=99, kitty=50)
animal_items = animals.items()
print(f"{animal_items = }")
for animal, score in animal_items:
    print(f"{animal} has {score} mark")
```


```python
%reset -f
# Example on range

for i in range(10):
    print(i, end=' ')

# for _ in range(n):
#     ....

print("\n", "-"*10)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

```


#### More looping technique

**enumerate()**


```python
%reset -f

ivs = enumerate(['tic', 'tac', 'toe'])
# print(f"{list(ivs) = }")

for i, v in ivs: # iterator
    print(i, v)
```


**zip()**


```python
%reset -f

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print(f"{list(zip(questions, answers)) = }")

for q, a in zip(questions, answers): # iterator
    print('What is your {0}?  It is {1}.'.format(q, a))

```


**reversed()**


```python
%reset -f

for i in reversed(range(1, 10, 2)): # iterator
    print(i)
```


**sorted()**


```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket): # list (not iterator)
    print(i)

```


#### List, Set, Dictionary Comprehension

##### List comprehension

**Problem.** Create a list of squares of first n number (example, n = 10).
- Newbie way
```python
squares = []
for x in range(10):
    squares.append(x**2)
```

- Use builtin function `map()`
```python
squares = list(map(lambda x: x**2, range(10)))
```

- Use list comprehension  
```python
squares = [x**2 for x in range(10)]
```

**Syntax:** `[<expression> for <var_list> in <iterable> [for <var_list_inner> in <iterable_inner> ...] [if <condition>]]`  
**Expand form:**
```python
l = []
for <var_list> in <iterable>:
    [for <var_list_inner> in <iterable_inner>:
        ...]
        [if <condition>:]
            l.append(<expression>)
```



```python
%reset -f
# Example list comprehension

l1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(f"{l1 = }")

vec = [[1,2,3], [4,5,6], [7,8,9]]
l2 = [num for elem in vec for num in elem]
print(f"{l2 = }")

l3 = [(f"ord({c})", ord(c)) for c in "qwerty"]
print(f"{l3 = }")

l4 = ["zero" if x - y == 0 else "negative" if x - y > 0 else "positive" for x in range(4) for y in range(4) if abs(x - y) < 2]
print(f"{l4 = }")

# Nested
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
l5 = [[row[i] for row in matrix] for i in range(4)]
print("Transpose: ", *l5, sep='\n ')

# ~ list(zip(*matrix))
```


#### Set comprehension

Similarly to list comprehensions


```python
%reset -f
# Example

a = {x for x in 'abracadabra' if x not in 'abc'}
print(f"{a = }")

```


#### Dictionary comprehension

Similarly to list comprehensions, but use `<key_expression>: <value_expression>` instead of `<expression>` inf list comprehension. 


```python
%reset -f
# Example

d = {x: x**2 for x in (2, 4, 6)}
print(f"{d = }")
```


### `break` and `continue` Statement

- The `break` statement breaks out of the innermost enclosing `for` or `while` loop.
- The `continue` statement continues with the next iteration of the loop.

> **Tip:** when we want to break all loop, to simplify, we should use function and return when you need break. Or you can use `else` statement if it's better.



```python
%reset -f
# Example
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
        
```


```python
%reset -f
# Example
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
```


### `else` Clauses on Loops

- In a `for` loop, the `else` clause is executed after the loop finishes its final iteration, that is, if no break occurred.
- In a `while` loop, it’s executed after the loop’s condition becomes false.
- In either kind of loop, the `else` clause is not executed if the loop was terminated by a break.
- Other ways of ending the loop early, such as a **return** or a **raised exception**, will also skip execution of the `else` clause.


```python
%reset -f
# Example

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

```


### `pass` Statement

The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.



```python
%reset -f
# Example

for i in range(1000):
    pass

```


### `match` Statement

- This is superficially similar to a **`switch` statement** in C, Java or JavaScript (and many other languages), but it’s more similar to **pattern matching** in languages like Rust or Haskell.
- Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.

**Syntax:**
```python
match <expression>:
    case <pattern_1> [if <expression>]:
        <statement>
        ...
    [...
    case <pattern_n> [if <expression>]::
        <statement>
        ...
    [case _ [if <expression>]:
        <statement>
        ...
    ]]
```

**`if <expression>`** after pattern called **guard**.
**`_`** is a wildcard.

**Patterns:**
- Literals
- Variables
- Combine of single patterns with `|`
- Sequences pattern.
- Mapping patterns.
- Unpack class object `<expression>` pattern.

For more about **pattern** see [here](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
Learn more about `match` see [here](https://docs.python.org/3/tutorial/controlflow.html#match-statements)



```python
%reset -f
# Example

status = 500

match status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case 401 | 402 | 403:
        print("Not allowed")
    case x if x < 400:
        print("In valid range")
    case _:
        print("Something's wrong with the internet")

```


```python
%reset -f
# Example

point = (0, 20)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case x, 0:
        print(f"X={x}")
    case x, y:
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```


```python
%reset -f
# Example

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(10, 0)

match point:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=0, y=y):
        print(f"Y={y}")
    case Point(x=x, y=0):
        print(f"X={x}")
    case Point():
        print("Somewhere else")
    case _:
        print("Not a point")
```


```python
%reset -f
# Example

point = (1, 2, 1, 0)

match point:
    case (0, 0, *rest):
        print(f"Both axis 0 and axis 1 is equal to 0 and rest of point is {rest}")
    
    case (x, 0, *_) | (0, x, *_):
        print(f"Axis 0 and axis 1 has only one non zero with value = {x}")
    
    case (x, y, *_) if x == y:
        print("axis 0 value is same as axis 1 value")
    
    case _:
        print(f"{point = }")
```


```python
%reset -f
# Example

d = {'ichi': 2, 'san': 3, 'yon': 1, 'ni': 4}

match d:
    case {'ichi': 1}:
        print('ichi is true')
    
    case {'ni': 2}:
        print('ni is true')
    
    case {'san': 3, **rest}:
        print('san is true')
        print(f"{rest = }")
    
    case {'yon': 4, **rest}:
        print('yon is true')
        print(f"{rest = }")
        
```


### Function

#### Defining Function

**Syntax:**
```python
def <function_name>([<parameter_list>]):
    [<docstring>]
    <statement>
    ...
    [return <return_value>]
```

- The execution of a function introduces a new **symbol table** used for the **local variables** of the function.
- A function definition associates the function name with the function object in the current symbol table.
- Functions without a `return` statement do return a value, albeit a rather boring one. This value is called `None`.
- Function nested in function is valid.
 


```python
%reset -f
# Exmample
def fib(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f = fib

f100 = f(100)        # call it
print(f"{f100 = }")  # write the result
```


#### Default Argument Values

- The default values are evaluated at the point of function definition in the defining scope
- The default value is evaluated only once.



```python
%reset -f
# Example
val = 2
def f(a = val, L=[]):
    L.append(a)
    return L

val = 1
print(f())
print(f(3))
print(f(5))
```


#### Keyword Arguments

`kwarg=value`

Exmaple:
```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, 
```

Valid call:
```python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 ke
```

Invalid call:
```python
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argum
```
entyword"!")


```python
%reset -f
# Example

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(voltage=1000000, action='VOOOOOM')             
parrot(action='VOOOOOM', voltage=1000000)             
parrot('a million', 'bereft of life', 'jump')  
```

**Special parameters**

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
        -- Positional only
```



```python
%reset -f
# Example

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg("standard_arg")
standard_arg(arg="standard_arg")

pos_only_arg("pos_only_arg")

kwd_only_arg(arg="kwd_only_arg")

combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
```


#### Unpacking Argument Lists

- With set, list, tuple, use `*` to pass to *pos_arg*.
- With dictionary use `**` to pass to *kwd_arg*.



```python
%reset -f
# Example

def f(a, b, c, d):
    print(f"{a = }, {b = }, {c = }, {d = }")

s = {1}
l = [2, 3]
t = (4, 5, 6)
d1 = {"d": 7}
d2 = {"b": 8, "c": 9}

f(*l, *s, **d1)
f(*t, **d1)
f(*s, **d1, **d2)
```


#### Arbitrary Argument Lists

- Use `*` in parameter list to pack remain posional argument.
- Use `**` in parameter list to pack remain keyword argument.

> After `*` parameter is keyword-only parameter.
> No parameter define after `**` parameter.


```python
%reset -f
# Example

def f(a, *b, c, **d):
    print(f"{a = }, {b = }, {c = }, {d = }")

f(1, e=1, c=2, s=3)
f(1, 2, 3, e=1, c=2, s=3)

d1 = {'e': 1, 'c': 2, 's': 3}
d2 = {'d': 4, 'b': 5}
t1 = (7, 8)
t2 = (9, 0)
f(*t1, *t2, **d2, **d1)
```

**Problem:**
```python
def foo(name, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
```

**Solution:**
```python
def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
```

#### Lambda Expressions

Small anonymous functions can be created with the lambda keyword.  
**Syntax:** `lambda <parameter_list>: <expression>`

> All about python's expression syntax, check [here](https://docs.python.org/3/reference/expressions.html).



```python
%reset -f
# Example

f = lambda a, / ,*b, c, **d: f"{a = }, {b = }, {c = }, {d = }"

d1 = {'e': 1, 'c': 2, 's': 3}
d2 = {'d': 4, 'b': 5}
t1 = (7, 8)
t2 = (9, 0)
print(f(*t1, *t2, **d2, **d1))

strs = ["hello", "help", "hi", "list", "tuple"]
strs.sort(key = lambda item: sorted(list(item)))
print(strs)
```


### More reference stuff

#### Documentation Strings

Please check [here](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)

#### Function Annotations

Please check [here](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)  
Example:
```python
def fib(n : int | float = 10) -> list[int]:  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
```

#### Intermezzo: Coding Style

For Python, [PEP 8](https://peps.python.org/pep-0008/) has emerged as the style guide that most projects adhere to, here are the most important points extracted:
- Use 4-space indentation, and no tabs.
- Wrap lines so that they don’t exceed 79 characters.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.
- When possible, put comments on a line of their own.
- Use docstrings.
- Use spaces around operators and after commas, but not directly inside bracketing constructs.
- Name your classes and functions consistently; the convention is to use `UpperCamelCase` for classes and `lowercase_with_underscores` for functions and methods. Always use `self` as the name for the first method argument.
- Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.
- Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.





```python

```
