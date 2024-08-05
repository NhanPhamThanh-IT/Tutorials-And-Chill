# Dynamic SQL

**Prerequisite** – Difference between Static and Dynamic

__Dynamic SQL__ is a programming technique that could be used to write SQL queries during runtime. Dynamic SQL could be used to create general and flexible SQL queries.

Syntax for dynamic SQL is to make it string as below:

```sql
'SELECT statement';
```

To run a dynamic SQL statement, run the stored procedure __sp_executesql__ as shown below:

```sql
EXEC sp_executesql N'SELECT statement';
```

Use prefix N with the sp_executesql to use dynamic SQL as a Unicode string.

## Steps to use Dynamic SQL

**1. Declare two variables, @var1 for holding the name of the table and @var 2 for holding the dynamic SQL:**

```sql
DECLARE 
@var1 NVARCHAR(MAX), 
@var2 NVARCHAR(MAX);
```

**2. Set the value of the @var1 variable to table_name:**

```sql
SET @var1 = N'table_name';
```

**3. Create the dynamic SQL by adding the SELECT statement to the table name parameter:**

```sql
SET @var2= N'SELECT * 
FROM ' + @var1;
```

**4. Run the sp_executesql stored procedure by using the @var2 parameter:**

```sql
EXEC sp_executesql @var2;
```

## Example

**Geek table**

| ID | NAME  | CITY   |
|----|-------|--------|
| 1  | Khushi| Jaipur |
| 2  | Neha  | Noida  |
| 3  | Meera | Delhi  |

**Example**

```sql
SELECT * FROM Geek;
```

**Using Dynamic SQL**

```sql
DECLARE 
@tab NVARCHAR(128), 
@st NVARCHAR(MAX);
SET @tab = N'geektable';
SET @st = N'SELECT * 
FROM ' + @tab;
EXEC sp_executesql @st;
```
