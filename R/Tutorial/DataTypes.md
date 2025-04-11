<div align='justify'>

# <div align='center'>Data Types</div>

Generally, while doing programming in any programming language, you need to use various variables to store various information. Variables are nothing but reserved memory locations to store values. This means that, when you create a variable you reserve some space in memory.

You may like to store information of various data types like character, wide character, integer, floating point, double floating point, Boolean etc. Based on the data type of a variable, the operating system allocates memory and decides what can be stored in the reserved memory.

In contrast to other programming languages like C and java in R, the variables are not declared as some data type. The variables are assigned with R-Objects and the data type of the R-object becomes the data type of the variable. There are many types of R-objects. The frequently used ones are:

- Vectors
- Lists
- Matrices
- Arrays
- Factors
- Data Frames

The simplest of these objects is the __vector object__ and there are six data types of these atomic vectors, also termed as six classes of vectors. The other R-Objects are built upon the atomic vectors.

<table align='center'>
    <tr align='center'>
        <th>Data Type</th>
        <th>Example</th>
    </tr>
    <tr align='center'>
        <td>Logical</td>
        <td>TRUE, FALSE</td>
    </tr>
    <tr align='center'>
        <td>Numeric</td>
        <td>12.3, 5, 999</td>
    </tr>
    <tr align='center'>
        <td>Integer</td>
        <td>2L, 34L, 0L</td>
    </tr>
    <tr align='center'>
        <td>Complex	</td>
        <td>3 + 2i</td>
    </tr>
    <tr align='center'>
        <td>Character</td>
        <td>'a' , '"good", "TRUE", '23.4'</td>
    </tr>
    <tr align='center'>
        <td>Raw</td>
        <td>"Hello" is stored as 48 65 6c 6c 6f</td>
    </tr>
</table>

You can use the following code to verify(show) the data type of one variable:

```R
v <- TRUE
print(class(v))
```

After running this code, we will get the below outcome:

```bash
[1] "logical"
```

The above code is the example to show how to verify the datatype of a Logical datatype. You can do the same for the other datatypes.

In R programming, the very basic data types are the R-objects called __vectors__ which hold elements of different classes as shown above. Please note in R the number of classes is not confined to only the above six types. For example, we can use many atomic vectors and create an array whose class will become array.

### Part 1 - Vectors

When you want to create vector with more than one element, you should use c() function which means to combine the elements into a vector.

```R
# Create a vector.
apple <- c('red','green',"yellow")
print(apple)

# Get the class of the vector.
print(class(apple))
```

When we execute the above code, it produces the following result:

```bash
[1] "red"    "green"  "yellow"
[1] "character"
```

### Part 2 - Lists

A list is an R-object which can contain many different types of elements inside it like vectors, functions and even another list inside it.

```R
# Create a list.
list1 <- list(c(2,5,3),21.3,sin)

# Print the list.
print(list1)
```

When we execute the above code, it produces the following result:

```bash
[[1]]
[1] 2 5 3

[[2]]
[1] 21.3

[[3]]
function (x) .Primitive("sin")
```

### Part 3 - Matrices

A matrix is a two-dimensional rectangular data set. It can be created using a vector input to the matrix function.

```R
# Create a matrix.
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
print(M)
```

When we execute the above code, it produces the following result:

```bash
    [,1] [,2] [,3]
[1,] "a"  "a"  "b" 
[2,] "c"  "b"  "a"
```

### Part 4 - Arrays

While matrices are confined to two dimensions, arrays can be of any number of dimensions. The array function takes a dim attribute which creates the required number of dimension. In the below example we create an array with two elements which are 3x3 matrices each.

```R
# Create an array.
a <- array(c('green','yellow'),dim = c(3,3,2))
print(a)
```

When we execute the above code, it produces the following result:

```bash
, , 1

     [,1]     [,2]     [,3]    
[1,] "green"  "yellow" "green" 
[2,] "yellow" "green"  "yellow"
[3,] "green"  "yellow" "green" 

, , 2

     [,1]     [,2]     [,3]    
[1,] "yellow" "green"  "yellow"
[2,] "green"  "yellow" "green" 
[3,] "yellow" "green"  "yellow"
```

### Part 5 - Factors

Factors are the r-objects which are created using a vector. It stores the vector along with the distinct values of the elements in the vector as labels. The labels are always character irrespective of whether it is numeric or character or Boolean etc. in the input vector. They are useful in statistical modeling.

Factors are created using the __factor()__ function. The __nlevels__ functions gives the count of levels.

```R
# Create a vector.
apple_colors <- c('green','green','yellow','red','red','red','green')

# Create a factor object.
factor_apple <- factor(apple_colors)

# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))
```

When we execute the above code, it produces the following result:

```bash
[1] green  green  yellow red    red    red    green 
Levels: green red yellow
[1] 3
```

### Part 6 - Data Frames

Data frames are tabular data objects. Unlike a matrix in data frame each column can contain different modes of data. The first column can be numeric while the second column can be character and third column can be logical. It is a list of vectors of equal length.

Data Frames are created using the __data.frame()__ function.

```R
# Create the data frame.
BMI <- 	data.frame(
   gender = c("Male", "Male","Female"), 
   height = c(152, 171.5, 165), 
   weight = c(81,93, 78),
   Age = c(42,38,26)
)
print(BMI)
```

When we execute the above code, it produces the following result:

```bash
  gender height weight Age
1   Male  152.0     81  42
2   Male  171.5     93  38
3 Female  165.0     78  26
```

</div>