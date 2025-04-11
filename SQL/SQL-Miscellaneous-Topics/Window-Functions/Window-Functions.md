# Window functions

Window functions apply to aggregate and ranking functions over a particular window (set of rows). OVER clause is used with window functions to define that window. OVER clause does two things : 

- Partitions rows to form a set of rows. (PARTITION BY clause is used) 
- Orders rows within those partitions into a particular order. (ORDER BY clause is used)

> [!NOTE]
>
> If partitions aren’t done, then ORDER BY orders all rows of the table. 

**Syntax**

```sql
SELECT column_name1, window_function(cloumn_name2)
OVER([PARTITION BY column_name1] [ORDER BY column_name3]) AS new_column
FROM table_name;
```

**Parameters**

> [!IMPORTANT]
> 
> window_function = any aggregate or ranking function    
> column_name1 = column to be selected
> column_name2 = column on which window function is to be applied
> column_name3 = column on whose basis partition of rows is to be done
> new_column = Name of new column
> table_name = Name of table

## Aggregate Window Function
Various aggregate functions such as SUM(), COUNT(), AVERAGE(), MAX(), and MIN() applied over a particular window (set of rows) are called aggregate window functions. 

Consider the following **employee** table:

| Name    | Age | Department | Salary  |
|---------|-----|------------|---------|
| Ramesh  | 20  | Finance    | 50,000  |
| Deep    | 25  | Sales      | 30,000  |
| Suresh  | 22  | Finance    | 50,000  |
| Ram     | 28  | Finance    | 20,000  |
| Pradeep | 22  | Sales      | 20,000  |

**Example**

Find average salary of employees for each department and order employees within a department by age.

```SQL
SELECT Name, Age, Department, Salary, 
      AVG(Salary) OVER (PARTITION BY Department) AS Avg_Salary
FROM employee;
```

This outputs the following:

| Name    | Age | Department | Salary  | Avg_Salary |
|---------|-----|------------|---------|------------|
| Ramesh  | 20  | Finance    | 50,000  | 40,000     |
| Suresh  | 22  | Finance    | 50,000  | 40,000     |
| Ram     | 28  | Finance    | 20,000  | 40,000     |
| Deep    | 25  | Sales      | 30,000  | 25,000     |
| Pradeep | 22  | Sales      | 20,000  | 25,000     |

Notice how all the average salaries in a particular window have the same value.

Let’s consider another case: 

```SQL
SELECT Name, Age, Department, Salary, 
      AVG(Salary) OVER (PARTITION BY Department ORDER BY Age) AS Avg_Salary
FROM employee;
```

Here we also order the records within the partition as per age values and hence the average values change as per the sorted order.

The output of above query will be :  

| Name    | Age | Department | Salary  | Avg_Salary |
|---------|-----|------------|---------|------------|
| Ramesh  | 20  | Finance    | 50,000  | 50,000     |
| Suresh  | 22  | Finance    | 50,000  | 50,000     |
| Ram     | 28  | Finance    | 20,000  | 40,000     |
| Pradeep | 22  | Sales      | 20,000  | 20,000     |
| Deep    | 25  | Sales      | 30,000  | 25,000     |

Hence, we should be careful while adding order by clauses to window functions with aggregates.

## Ranking Window Functions
Ranking functions are, RANK(), DENSE_RANK(), ROW_NUMBER()
- **RANK()** – As the name suggests, the rank function assigns rank to all the rows within every partition. Rank is assigned such that rank 1 given to the first row and rows having same value are assigned same rank. For the next rank after two same rank values, one rank value will be skipped. For instance, if two rows share­ rank 1, the next row gets rank 3, not 2.
- **DENSE_RANK()** – It assigns rank to each row within partition. Just like rank function first row is assigned rank 1 and rows having same value have same rank. The difference between RANK() and DENSE_RANK() is that in DENSE_RANK(), for the next rank after two same rank, consecutive integer is used, no rank is skipped.
- **ROW_NUMBER()** – ROW_NUMBER() gives e­ach row a unique number. It numbers rows from one­ to the total rows. The rows are put into groups base­d on their values. Each group is called a partition. In e­ach partition, rows get numbers one afte­r another. No two rows have the same­ number in a partition. This makes ROW_NUMBER() differe­nt from RANK() and DENSE_RANK(). ROW_NUMBER() uniquely identifies e­very row with a sequential inte­ger number. This helps with diffe­rent kinds of data analysis.

> [!NOTE]
>
> ORDER BY() should be specified compulsorily while using rank window functions.

**Example**
Calculate row no., rank, dense rank of employees is employee table according to salary within each department.

```SQL
SELECT 
      ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS emp_row_no, 
      Name,  
      Department, 
      Salary,
      RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS emp_rank,
      DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS emp_dense_rank
FROM 
      employee;
```

The output of above query will be:

| emp_row_no | Name    | Department | Salary  | emp_rank | emp_dense_rank |
|------------|---------|------------|---------|----------|----------------|
| 1          | Ramesh  | Finance    | 50,000  | 1        | 1              |
| 2          | Suresh  | Finance    | 50,000  | 1        | 1              |
| 3          | Ram     | Finance    | 20,000  | 3        | 2              |
| 1          | Deep    | Sales      | 30,000  | 1        | 1              |
| 2          | Pradeep | Sales      | 20,000  | 2        | 2              |

So, we can see that as mentioned in the definition of ROW_NUMBER() the row numbers are consecutive integers within each partition. Also, we can see difference between rank and dense rank that in dense rank there is no gap between rank values while there is gap in rank values after repeated rank.
