<div align="justify">

# <div align="center"><strong>Numbers</strong></div>

There are three numeric types in Python:

- int
- float
- complex

Variables of numeric types are created when you assign a value to them:

> __Example__
> 
> ```py
> x = 1    # int
> y = 2.8  # float
> z = 1j   # complex
> ```

To verify the type of any object in Python, use the `type()` function:

> __Example__
> 
> ```py
> print(type(x))
> print(type(y))
> print(type(z))
> ```

## Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

> __Example__
>
> Integers:
> 
> ```py
> x = 1
> y = 35656222554887711
> z = -3255522
>
> print(type(x))
> print(type(y))
> print(type(z))
> ```

## Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

> __Example__
>
> Floats:
>
> ```py
> x = 1.10
> y = 1.0
> z = -35.59
>
> print(type(x))
> print(type(y))
> print(type(z))
> ```

Float can also be scientific numbers with an "e" to indicate the power of 10.

> __Example__
>
> Floats:
>
> ```py
> x = 35e3
> y = 12E4
> z = -87.7e100
>
> print(type(x))
> print(type(y))
> print(type(z))
> ```

## Complex
Complex numbers are written with a "j" as the imaginary part:

> __Example__
>
> Complex:
>
> ```py
> x = 3+5j
> y = 5j
> z = -5j
>
> print(type(x))
> print(type(y))
> print(type(z))
> ```

## Type Conversion
You can convert from one type to another with the `int()`, `float()`, and `complex()` methods:

> __Example__
>
> Convert from one type to another:
>
> ```py
> x = 1    # int
> y = 2.8  # float
> z = 1j   # complex
>
> #convert from int to float:
> a = float(x)
>
> #convert from float to int:
> b = int(y)
>
> #convert from int to complex:
> c = complex(x)
>
> print(a)
> print(b)
> print(c)
>
> print(type(a))
> print(type(b))
> print(type(c))
> ```

__Note:__ You cannot convert complex numbers into another number type.

## Random Number
Python does not have a `random()` function to make a random number, but Python has a built-in module called `random` that can be used to make random numbers:

> __Example__
>
> Import the random module, and display a random number from 1 to 9:
>
> ```py
> import random
>
> print(random.randrange(1, 10))
> ```

__Note__: In my Random Module Reference you will learn more about the Random module.

</div>