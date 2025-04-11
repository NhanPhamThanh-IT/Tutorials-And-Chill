<div align='justify'>

# <div align='center'>Functions</div>

A function is a set of statements organized together to perform a specific task. R has a large number of in-built functions and the user can create their own functions.

In R, a function is an object so the R interpreter is able to pass control to the function, along with arguments that may be necessary for the function to accomplish the actions.

The function in turn performs its task and returns control to the interpreter as well as any result which may be stored in other objects.

### Part 1 - Function Definition

An R function is created by using the keyword __function__. The basic syntax of an R function definition is as follows:

```R
function_name <- function(arg_1, arg_2, ...) {
   Function body 
}
```

### Part 2 - Function Components

The different parts of a function are:

- __Function Name__ − This is the actual name of the function. It is stored in R environment as an object with this name.
- __Arguments__ − An argument is a placeholder. When a function is invoked, you pass a value to the argument. Arguments are optional; that is, a function may contain no arguments. Also arguments can have default values.
- __Function Body__ − The function body contains a collection of statements that defines what the function does.
- __Return Value__ − The return value of a function is the last expression in the function body to be evaluated.

R has many __in-built__ functions which can be directly called in the program without defining them first. We can also create and use our own functions referred as __user defined__ functions.

### Part 3 - Built-in Function

Simple examples of in-built functions are __seq()__, __mean()__, __max()__, __sum(x)__ and __paste(...)__ etc. They are directly called by user written programs. You can refer most widely used R functions.

```R
# Create a sequence of numbers from 32 to 44.
print(seq(32,44))

# Find mean of numbers from 25 to 82.
print(mean(25:82))

# Find sum of numbers frm 41 to 68.
print(sum(41:68))
```

When we execute the above code, it produces the following result:

```bash
[1] 32 33 34 35 36 37 38 39 40 41 42 43 44
[1] 53.5
[1] 1526
```

### Part 4 - User-defined Function

We can create user-defined functions in R. They are specific to what a user wants and once created they can be used like the built-in functions. Below is an example of how a function is created and used.

```R
# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
   for(i in 1:a) {
      b <- i^2
      print(b)
   }
}
```

### Part 5 - Calling a Function

```R
# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
   for(i in 1:a) {
      b <- i^2
      print(b)
   }
}

# Call the function new.function supplying 6 as an argument.
new.function(6)
```

When we execute the above code, it produces the following result:

```bash
[1] 1
[1] 4
[1] 9
[1] 16
[1] 25
[1] 36
```

### Part 6 - Calling a Function without an Argument

```R
# Create a function without an argument.
new.function <- function() {
   for(i in 1:5) {
      print(i^2)
   }
}	

# Call the function without supplying an argument.
new.function()
```

When we execute the above code, it produces the following result:

```bash
[1] 1
[1] 4
[1] 9
[1] 16
[1] 25
```

### Part 7 - Calling a Function with Argument Values (by position and by name)

The arguments to a function call can be supplied in the same sequence as defined in the function or they can be supplied in a different sequence but assigned to the names of the arguments.

```r
# Create a function with arguments.
new.function <- function(a,b,c) {
   result <- a * b + c
   print(result)
}

# Call the function by position of arguments.
new.function(5,3,11)

# Call the function by names of the arguments.
new.function(a = 11, b = 5, c = 3)
```

When we execute the above code, it produces the following result:

```bash
[1] 26
[1] 58
```

### Part 8 - Calling a Function with Default Argument

We can define the value of the arguments in the function definition and call the function without supplying any argument to get the default result. But we can also call such functions by supplying new values of the argument and get non default result.

```r
# Create a function with arguments.
new.function <- function(a = 3, b = 6) {
   result <- a * b
   print(result)
}

# Call the function without giving any argument.
new.function()

# Call the function with giving new values of the argument.
new.function(9,5)
```

When we execute the above code, it produces the following result:

```bash
[1] 18
[1] 45
```

### Part 9 - Lazy Evaluation of Function

Arguments to functions are evaluated lazily, which means so they are evaluated only when needed by the function body.

```r
# Create a function with arguments.
new.function <- function(a, b) {
   print(a^2)
   print(a)
   print(b)
}

# Evaluate the function without supplying one of the arguments.
new.function(6)
```

When we execute the above code, it produces the following result:

```bash
[1] 36
[1] 6
Error in print(b) : argument "b" is missing, with no default
```

</div>