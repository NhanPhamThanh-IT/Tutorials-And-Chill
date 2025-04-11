# Stored Procedures
A stored procedure in SQL is a group of SQL queries that can be saved and reused multiple times. It is very useful as it reduces the need for rewriting SQL queries. It enhances efficiency, reusability, and security in database management.

Users can also pass parameters to stored procedures so that the stored procedure can act on the passed parameter values.

Stored Procedures are created to perform one or more DML operations on the Database. It is nothing but a group of **SQL statements** that accepts some input in the form of parameters, performs some task, and may or may not return a value. 

## Syntax
Two important syntaxes for using stored procedures in SQL are:

**Syntax to Create a Stored Procedure**

> [!IMPORTANT]
> 
>     CREATE PROCEDURE procedure_name
>
>     (parameter1 data_type, parameter2 data_type, …)
>
>     AS
>
>     BEGIN
>
>         — SQL statements to be executed
>
>     END

**Syntax to Execute the Stored Procedure**

> [!IMPORTANT]
> 
>     EXEC procedure_name parameter1_value, parameter2_value, ..

**Parameter**
The most important part is the parameters. Parameters are used to pass values to the Procedure. There are different types of parameters, which are as follows: 

1. **BEGIN**: This is what directly executes or we can say that it is an executable part.
2. **END**: Up to this, the code will get executed.

## SQL Stored Procedure Example
Let’s look at an example of Stored Procedure in SQL to understand it better.

Imagine a database named “SampleDB”, a table named “Customers” with some sample data, and a stored procedure named” GetCustomersByCountry”.

The stored procedure takes the parameter “Country” and returns a list of customers from the “Customers” table that matches the specified country. Finally, the stored procedure is executed with the parameter “Sri Lanka” to retrieve the list of customers from Sri Lanka.

**Query**

> [!IMPORTANT]
> Create a new database named "SampleDB"
>
>      CREATE DATABASE SampleDB;
>
> Switch to the new database
>
>     USE SampleDB;
>
> Create a new table named "Customers"
>
>     CREATE TABLE Customers (
>
>         CustomerID INT PRIMARY KEY,
>
>         CustomerName VARCHAR(50),
>
>         ContactName VARCHAR(50),
>
>         Country VARCHAR(50)
>
>     );
>
> Insert some sample data into the Customers table
>
>     INSERT INTO Customers (CustomerID, CustomerName, ContactName, Country)
>
>     VALUES
>
>             (1, 'Shubham', 'Thakur', 'India'),
>
>             (2, 'Aman ', 'Chopra', 'Australia'),
>
>             (3, 'Naveen', 'Tulasi', 'Sri lanka'),
>
>             (4, 'Aditya', 'Arpan', 'Austria'),
>
>             (5, 'Nishant. Salchichas S.A.', 'Jain', 'Spain');
>
> Create a stored procedure named "GetCustomersByCountry"
>
>     CREATE PROCEDURE GetCustomersByCountry
>
>     @Country VARCHAR(50)
>
>     AS
>
>     BEGIN
>
>         SELECT CustomerName, ContactName
>
>         FROM Customers
>
>         WHERE Country = @Country;
>
>     END;
>
> Execute the stored procedure with parameter "Sri lanka"
>
>     EXEC GetCustomersByCountry @Country = 'Sri lanka';

**Note**: You will need to make sure that the user account has the necessary privileges to create a database. You can try logging in as a different user with administrative privileges or contact the database administrator to grant the necessary privileges to your user account. If you are using a cloud-based database service, make sure that you have correctly configured the user account and its permissions.

**Output**
| CustomerName | Contact Name |
|--------------|--------------|
|    Naveen    |    Tulasi    |

## Important Points About SQL Stored Procedures

- A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.
- Stored procedures allow for code that is used repeatedly to be saved on the database and run from there, rather than from the client. This provides a more modular approach to database design.
- Since stored procedures are compiled and stored in the database, they are highly efficient. SQL Server compiles each stored procedure once and then reutilizes the execution plan. This leads to tremendous performance boosts when stored procedures are called repeatedly.
- Stored procedures provide better security to your data. Users can execute a stored procedure without needing to execute any of the statements directly. Therefore, a user can be granted permission to execute a stored procedure without having any permissions on the underlying tables.
- Stored procedures can reduce network traffic and latency, boosting application performance. A single call to a stored procedure can execute many statements.
- Stored procedures have better support for error handling.
- Stored procedures can be used to provide advanced database functionality, such as modifying data in tables, and encapsulating these changes within database transactions.
