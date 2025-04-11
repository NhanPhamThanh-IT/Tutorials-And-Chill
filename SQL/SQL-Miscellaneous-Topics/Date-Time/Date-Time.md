# How to Get Current Date and Time in SQL?
There are many built-in functions to get the current date and time in SQL. In this article, we will discuss how to get the current date and time in SQL with examples.

## SQL Get Current Date and Time
Three in-built SQL functions to fetch current date and time are:

- SQL GETDATE() Function
- SQL CURRENT_TIMESTAMP() Function
- SQL SYSDATETIME() Function

## SQL GETDATE() Function
**SQL GETDATE() function** returns the current database system date and time in the format ‘YYYY-MM-DD hh:mm: ss. mmm’.

**Syntax**

The GETDATE() function syntax is:

```SQL
SELECT GETDATE();
```

**Example**

In this example, we use the GetDate() function in SQL to get the current date and time.

**Query**

```SQL
SELECT GetDate() AS 'CurrentDATETime';
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20211001112815/x.png)

## Get Only Time Part from GETDATE() Function Example

In this example, we will get only the time part from the GETDATE() function in SQL.

**Query**

```SQL
SELECT CONVERT(VARCHAR(8), GETDATE(),108)'hh:mi:ss'
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20211001114854/uploaded_file.png)

## SQL CURRENT_TIMESTAMP() Function

**SQL CURRENT_TIMESTAMP() function** used to find the current TIMESTAMP (current Date and Time). The CURRENT_TIMESTAMP returns the same result as **GETDATE()**.

**Syntax**

The CURRENT_TIMESTAMP() function syntax is:

```sql
CURRENT_TIMESTAMP
```

**Example**

In this example, we use the CURRENT_TIMESTAMP() function in SQL to get the current date and time.

**Query**

```sql
SELECT CURRENT_TIMESTAMP AS "CURRENTTIMESTAMP"; 
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20211001113609/v.png)

## SQL SYSDATETIME() Function

**SQL SYSDATETIME()** function is also used to get the current time of the System on which the instance of SQL Server is running. SYSDATETIME() function provides more fractional seconds precision compared to the GETDATE() function.

We can fetch the TIME part from the DATE and TIME value returned from the SYSDATETIME() function as below:

**Syntax**

The __SYSDATETIME()__ function syntax is:

```sql
SYSDATETIME()
```

**Example**

In this example, we use the SYSDATETIME() function in SQL to get the current date and time.

**Query**

```sql
SELECT SYSDATETIME() 'Current TIME using SYSDATETIME()'
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20211001114052/n-300x122.png)
