<div align="justify">

# <div align="center">Strings</div>

## Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

`'hello'` is the same as `"hello"`.

You can display a string literal with the `print()` function:

> __Example__
>
> ```py
> print("Hello")
> print('Hello')
> ```

## Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

> __Example__
>
> ```py
> print("It's alright")
> print("He is called 'Johnny'")
> print('He is called "Johnny"')
> ```

## Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

> __Example__
>
> ```py
> a = "Hello"
> print(a)
> ```

## Multiline Strings
You can assign a multiline string to a variable by using three quotes:

> __Example__
>
> You can use three double quotes:
>
> ```py
> a = """Lorem ipsum dolor sit amet,
> consectetur adipiscing elit,
> sed do eiusmod tempor incididunt
> ut labore et dolore magna aliqua."""
> print(a)
> ```

Or three single quotes:

> __Example__
>
> ```py
> a = '''Lorem ipsum dolor sit amet,
> consectetur adipiscing elit,
> sed do eiusmod tempor incididunt
> ut labore et dolore magna aliqua.'''
> print(a)
> ```

__Note:__ in the result, the line breaks are inserted at the same position as in the code.

## Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

> __Example__
>
> ```py
> a = "Hello, World!"
> print(a[1])
> ```

## Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a `for` loop.

> __Example__
>
> ```py
> for x in "banana":
>   print(x)
> ```

Learn more about For Loops in my `For Loops` chapter.

## String Length
To get the length of a string, use the `len()` function.

> __Example__
>
> ```py
> a = "Hello, World!"
> print(len(a))
> ```

## Check String
To check if a certain phrase or character is present in a string, we can use the keyword `in`.

> __Example__
>
> ```py
> txt = "The best things in life are free!"
> print("free" in txt)
> ```

Use it in an `if` statement:

> __Example__
>
> ```py
> txt = "The best things in life are free!"
> if "free" in txt:
>   print("Yes, 'free' is present.")
> ```

Learn more about If statements in our `If...Else` chapter.

## Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.

> __Example__
>
> ```py
> txt = "The best things in life are free!"
> print("expensive" not in txt)
> ```

Use it in an `if` statement:

> __Example__
>
> ```py
> txt = "The best things in life are free!"
> if "expensive" not in txt:
>   print("No, 'expensive' is NOT present.")
> ```


</div>