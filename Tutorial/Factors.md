<div align='justify'>

# <div align='center'>Factors</div>

Factors are the data objects which are used to categorize the data and store it as levels. They can store both strings and integers. They are useful in the columns which have a limited number of unique values. Like "Male, "Female" and True, False etc. They are useful in data analysis for statistical modeling.

Factors are created using the __factor ()__ function by taking a vector as input.

### Example

```r
# Create a vector as input.
data <- c("East","West","East","North","North","East","West","West","West","East","North")

print(data)
print(is.factor(data))

# Apply the factor function.
factor_data <- factor(data)

print(factor_data)
print(is.factor(factor_data))
```

When we execute the above code, it produces the following result:

```bash
[1] "East"  "West"  "East"  "North" "North" "East"  "West"  "West"  "West"  "East" "North"
[1] FALSE
[1] East  West  East  North North East  West  West  West  East  North
Levels: East North West
[1] TRUE
```

## Factors in Data Frame

On creating any data frame with a column of text data, R treats the text column as categorical data and creates factors on it.

```r
# Create the vectors for data frame.
height <- c(132,151,162,139,166,147,122)
weight <- c(48,49,66,53,67,52,40)
gender <- c("male","male","female","female","male","female","male")

# Create the data frame.
input_data <- data.frame(height,weight,gender)
print(input_data)

# Test if the gender column is a factor.
print(is.factor(input_data$gender))

# Print the gender column so see the levels.
print(input_data$gender)
```

When we execute the above code, it produces the following result:

```bash
  height weight gender
1    132     48   male
2    151     49   male
3    162     66 female
4    139     53 female
5    166     67   male
6    147     52 female
7    122     40   male
[1] TRUE
[1] male   male   female female male   female male  
Levels: female male
```

## Changing the Order of Levels

The order of the levels in a factor can be changed by applying the factor function again with new order of the levels.

```r
data <- c("East","West","East","North","North","East","West",
   "West","West","East","North")
# Create the factors
factor_data <- factor(data)
print(factor_data)

# Apply the factor function with required order of the level.
new_order_data <- factor(factor_data,levels = c("East","West","North"))
print(new_order_data)
```

When we execute the above code, it produces the following result:

```bash
 [1] East  West  East  North North East  West  West  West  East  North
Levels: East North West
 [1] East  West  East  North North East  West  West  West  East  North
Levels: East West North
```

## Generating Factor Levels

We can generate factor levels by using the __gl()__ function. It takes two integers as input which indicates how many levels and how many times each level.

### Syntax

```r
gl(n, k, labels)
```

Following is the description of the parameters used:

- __n__ is a integer giving the number of levels.
- __k__ is a integer giving the number of replications.
- __labels__ is a vector of labels for the resulting factor levels.

### Example

```r
v <- gl(3, 4, labels = c("Tampa", "Seattle","Boston"))
print(v)
```

When we execute the above code, it produces the following result:

```bash
Tampa   Tampa   Tampa   Tampa   Seattle Seattle Seattle Seattle Boston 
[10] Boston  Boston  Boston 
Levels: Tampa Seattle Boston
```

</div>