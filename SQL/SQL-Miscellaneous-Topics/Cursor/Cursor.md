# What is Cursor in SQL?

__Cursor__ is a Temporary Memory or Temporary Work Station. It is Allocated by Database Server at the Time of Performing DML(Data Manipulation Language) operations on the Table by the User. Cursors are used to store Database Tables. 

There are 2 types of Cursors: Implicit Cursors, and Explicit Cursors. These are explained as following below.

1. __Implicit Cursors__: Implicit Cursors are also known as Default Cursors of SQL SERVER. These Cursors are allocated by SQL SERVER when the user performs DML operations.
2. __Explicit Cursors__: Explicit Cursors are Created by Users whenever the user requires them. Explicit Cursors are used for Fetching data from Table in Row-By-Row Manner.

## How To Create Explicit Cursor?

__1. Declare Cursor Object__

**Syntax**

```sql
DECLARE cursor_name CURSOR FOR SELECT * FROM table_name
```

**Query**

```sql
DECLARE s1 CURSOR FOR SELECT * FROM studDetails
```

__2. Open Cursor Connection__

**Syntax**

```sql
OPEN cursor_connection
```

**Query**

```sql
OPEN s1
```

**Fetch Data from the Cursor**: There is a total of 6 methods to access data from the cursor. They are as follows: 

1. **FIRST** is used to fetch only the first row from the cursor table. 
2. **LAST** is used to fetch only the last row from the cursor table. 
3. **NEXT** is used to fetch data in a forward direction from the cursor table. 
4. **PRIOR** is used to fetch data in a backward direction from the cursor table. 
5. **ABSOLUTE** n is used to fetch the exact nth row from the cursor table. 
6. **RELATIVE** n is used to fetch the data in an incremental way as well as a decremental way. 

**Syntax**

```sql
FETCH NEXT/FIRST/LAST/PRIOR/ABSOLUTE n/RELATIVE n FROM cursor_name
```

**Query**

```sql
FETCH FIRST FROM s1
FETCH LAST FROM s1
FETCH NEXT FROM s1
FETCH PRIOR FROM s1
FETCH ABSOLUTE 7 FROM s1
FETCH RELATIVE -2 FROM s1
```

- **Close cursor connection**

**Syntax**

```sql
CLOSE cursor_name
```

- **Deallocate cursor memory**

**Syntax**

```sql
DEALLOCATE cursor_name
```

**Query**

```sql
DEALLOCATE s1
```

## How To Create an Implicit Cursor?

An implicit cursor is a cursor that is automatically created by PL/SQL when you execute a SQL statement. You don’t need to declare or open an implicit cursor explicitly. Instead, PL/SQL manages the cursor for you behind the scenes.

To create an implicit cursor in PL/SQL, you simply need to execute a SQL statement. For example, to retrieve all rows from the EMP table, you can use the following code:

**Query**

```sql
BEGIN
    FOR emp_rec IN SELECT * FROM emp LOOP
        DBMS_OUTPUT.PUT_LINE('Employee name: ' || emp_rec.ename);
    END LOOP;
END;
```

In PL/SQL, when we perform INSERT, UPDATE or DELETE operations, an implicit cursor is automatically created. This cursor holds the data to be inserted or identifies the rows to be updated or deleted. You can refer to this cursor as the SQL cursor in your code. Thi SQL cursor has several useful attributes.

1. __%FOUND__ is true if the most recent SQL operation affected at least one row.
2. __%NOTFOUND__ is true if it didn’t affect any rows.
3. __%ROWCOUNT__ is returns the number of rows affected.
4. __%ISOPEN__ checks if the cursor is open.

In addition to these attributes, %BULK_ROWCOUNT and %BULK_EXCEPTIONS are specific to the FORALL statement, which is used to perform multiple DML operations at once. %BULK_ROWCOUNT returns the number of rows affected by each DML operation, while %BULK_EXCEPTION returns any exception that occurred during the operations.

**Query**

```sql
CREATE TABLE Emp(
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    Country VARCHAR(50),
    Age int(2),
  Salary int(10)
);
-- Insert some sample data into the Customers table
INSERT INTO Emp (EmpID, Name,Country, Age, Salary)
VALUES (1, 'Shubham',  'India','23','30000'),
       (2, 'Aman ',  'Australia','21','45000'),
       (3, 'Naveen', 'Sri lanka','24','40000'),
       (4, 'Aditya',  'Austria','21','35000'),
       (5, 'Nishant', 'Spain','22','25000');
       Select * from Emp;
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20230418121859/Screenshot_82.png)

This program updates a table by increasing the salary of each employee by 1500. After the update, the SQL%ROWCOUNT attribute is used to find out how many rows were affected by the operation.

**Query**

```sql
DECLARE  
      total_rows number; 
BEGIN 
      UPDATE Emp 
            SET Salary = Salary + 1500; 
      
      total_rows := SQL%ROWCOUNT;
      
      dbms_output.put_line(total_rows || ' rows updated.'); 
END;
```

**Output**

>
> 5 Emp selected  
> PL/SQL procedure successfully completed.

## SQL Cursor Exceptions

Whenever we execute an SQL query then there is the possibility of an error that is unexpected. Cursor goes through each set of rows to return in an SQL query.

There are some very popular exceptions:

1. __Duplicate Value__: This type of error occur when the cursor tries to insert a record or tuple which already exists in the database. these types of errors can be avoided by handling proper error conf
2. __Invalid Cursor State__: Whenever the cursor is in an invalid state this type of error will show as an error.
3. __Lock Timeout__: This occurs when the cursor tries to obtain a lock on a row or table but the lock is already held by another transaction.

## Need of Cursor in an SQL server

1. Cursors allow us to process data row-by-row, which can be useful when we need to perform complex calculations or transformations on the data.
2. Cursors allow us to iterate over a result set multiple times, which can be useful when we need to perform multiple operations on the same data.
3. Cursors can be useful when we need to join multiple tables with complex relationships, such as when processing hierarchical data structures or when performing recursive queries.
4. Cursors allow us to perform operations such as updating, deleting, or inserting records based on some condition or criteria.
5. Cursors are especially useful when processing data from multiple tables where the relationships are not straightforward.

## SQL Server Cursor Limitations
As a cursor has some limitations, it should only be used when there is no other choice. These restrictions include:

1. When processing data, it imposes locks on a subset or the entire table.
2. The cursor updates table records one row at a time, which slows down its performance.
3. While loops are slower than cursors, they do have more overhead.
4. Another factor that influences cursor speed is the quantity of rows and columns brought into the cursor.

## FAQ

__Question 1: How Can Cursors be Avoided?__

>
> __Cursors’ primary function is row-by-row table navigation. The following are some simple methods for avoiding cursors.__

__Question 2: How to Use While Loop in SQL Cursor?__

>
> __Using a while loop, which enables the insertion of a result set into the temporary table, is the simplest way to avoid the need for a cursor.__

__Question 3: What is User-defined functions in SQL Cursor?__

>
> __Sometimes the resultant row set is calculated using cursors. We can achieve this by employing a user-defined function that complies with the specifications.__

__Question 4: Use of Joins with SQL Cursor?__

>
> __In cases where huge records need to be processed, join reduces the number of lines of code by processing only those columns that meet the specified condition.__
