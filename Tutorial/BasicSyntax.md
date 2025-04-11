<div align='justify'>

# <div align='center'>Basic Syntax</div>

As a convention, we will start learning R programming by writing a "Hello, World!" program. Depending on the needs, you can program either at R command prompt or you can use an R script file to write your program. Let's check both one by one.

### Part 1 - R Command Prompt

Once you have R environment setup, then it’s easy to start your R command prompt by just typing the following command at your command prompt:

```bash
$ R
```

This will launch R interpreter and you will get a prompt > where you can start typing your program as follows:

```R
> myString <- "Hello, World!"
> print ( myString)
[1] "Hello, World!"
```

Here first statement defines a string variable myString, where we assign a string "Hello, World!" and then next statement print() is being used to print the value stored in variable myString.

### Part 2 - R Script File

Usually, you will do your programming by writing your programs in script files and then you execute those scripts at your command prompt with the help of R interpreter called __Rscript__. So let's start with writing following code in a text file called test.R as under:

```R
# My first program in R Programming
myString <- "Hello, World!"

print ( myString)
```

Save the above code in a file test.R and execute it at Linux command prompt as given below. Even if you are using Windows or other system, syntax will remain same.

```bash
$ Rscript test.R
```

When we run the above program, it produces the following result.

```bash
[1] "Hello, World!"
```

### Part 3 - Comments

Comments are like helping text in your R program and they are ignored by the interpreter while executing your actual program. Single comment is written using # in the beginning of the statement as follows:

```R
# My first program in R Programming
```

R does not support multi-line comments but you can perform a trick which is something as follows:

```R
if(FALSE) {
   "This is a demo for multi-line comments and it should be put inside either a 
      single OR double quote"
}

myString <- "Hello, World!"
print ( myString)
```

```bash
[1] "Hello, World!"
```

Though above comments will be executed by R interpreter, they will not interfere with your actual program. You should put such comments inside, either single or double quote.

</div>