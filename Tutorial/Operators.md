<div align='justify'>

# <div align='center'>Operators</div>

An operator is a symbol that tells the compiler to perform specific mathematical or logical manipulations. R language is rich in built-in operators and provides following types of operators.

### Part 1 - Types of Operators

We have the following types of operators in R programming:

- Arithmetic Operators
- Relational Operators
- Logical Operators
- Assignment Operators
- Miscellaneous Operators

### Part 2 - Arithmetic Operators

Following table shows the arithmetic operators supported by R language. The operators act on each element of the vector.

<table align='center'>
    <tr align='center'>
        <th>Operator</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td align='center'>+</td>
        <td align='center'>Adds two vectors</td>
        <td align='justify'>
            <pre>
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v+t)

[1] 10.0  8.5  10.0
            </pre>
        </td>
    </tr>
    <tr>
        <td align='center'>−</td>
        <td align='center'>Subtracts second vector from the first</td>
        <td align='justify'>
            <pre>
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v-t)

[1] -6.0  2.5  2.0
            </pre>
        </td>
    </tr>
    <tr>
        <td align='center'>\*</td>
        <td align='center'>Multiplies both vectors</td>
        <td align='justify'>
            <pre>
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v\*t)

[1] 16.0 16.5 24.0
            </pre>
        </td>
    </tr>
    <tr>
        <td align='center'>/</td>
        <td align='center'>Divide the first vector with the second</td>
        <td align='justify'>
            <pre>
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v/t)

[1] 0.250000 1.833333 1.500000
            </pre>
        </td>
    </tr>
    <tr>
        <td align='center'>%%</td>
        <td align='center'>Give the remainder of the first vector with the second</td>
        <td align='justify'>
            <pre>
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v%%t)

[1] 2.0 2.5 2.0
            </pre>
        </td>
    </tr>
    <tr>
        <td align='center'>%/%</td>
        <td align='center'>The result of division of first vector with second (quotient)</td>
        <td align='justify'>
            <pre>
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v%/%t)

[1] 0 1 1
            </pre>
        </td>
    </tr>
    <tr>
        <td align='center'>^</td>
        <td align='center'>The first vector raised to the exponent of second vector</td>
        <td align='justify'>
            <pre>
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v^t)

[1]  256.000  166.375 1296.000
            </pre>
        </td>
    </tr>
</table>

### Part 3 - Relational Operators

Following table shows the relational operators supported by R language. Each element of the first vector is compared with the corresponding element of the second vector. The result of comparison is a Boolean value.

</div>