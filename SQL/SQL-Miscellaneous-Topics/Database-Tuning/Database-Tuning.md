# Database Tuning

## SQL Database Tuning
Database Tuning in SQL is a set of activities performed to optimize a database and prevents it from becoming a bottleneck.

There are various techniques with which you can configure the optimal performance of a particular database. Database tuning overlaps with query tuning; so, good indexing and avoiding improper queries help in increasing the database efficiency. In addition, increasing storage, updating to latest database versions and investing in a more powerful CPU (if needed) are also some of the general techniques.

## Database Tuning Techniques
We can implement the following techniques to optimize the performance of a database.

## Database Normalization
Normalization is the process of removing of duplicate data from a database. We can normalize a database by breaking down larger tables into smaller related tables. This increases the performance of database as it requires less time to retrieve data from small tables instead of one large table.

## Proper Indexes
In SQL, indexes are the pointers (memory address) to the location of specific data in database. We use indexes in our database to reduce query time, as the database engine can jump to the location of a specific record using its index instead of scanning the entire database.

## Avoid Improper Queries
Choosing the correct query to retrieve data efficiently also improves the performance of a database. For example, choosing to retrieve an entire table when we only need the data in a single column will unnecessarily increase query time. So, query the database wisely.

Let us discuss some of the common improper queries made and how to rectify them to optimize the database performance.

### 1. Use SELECT fields instead of SELECT (*)
In large databases, we should always retrieve only the required columns from the database instead of retrieving all the columns, even when they are not needed. We can easily do this by specifying the column names in the SELECT statement instead of using the SELECT (*) statement.

**Example**

Assume we have created a table with name CUSTOMERS in MySQL database using CREATE TABLE statement as shown below:

```sql
CREATE TABLE CUSTOMERS (
     ID INT NOT NULL,
     NAME VARCHAR (20) NOT NULL,
     AGE INT NOT NULL,
     ADDRESS CHAR (25),
     SALARY DECIMAL (18, 2),       
     PRIMARY KEY (ID)
);
```

Following query inserts values into this table using the INSERT statement

```sql
INSERT INTO CUSTOMERS
VALUES 
    (1, 'Ramesh', 32, 'Ahmedabad', 2000.00 ),
    (2, 'Khilan', 25, 'Delhi', 1500.00 ),
    (3, 'Kaushik', 23, 'Kota', 2000.00 ),
    (4, 'Chaitali', 25, 'Mumbai', 6500.00 ),
    (5, 'Hardik', 27, 'Bhopal', 8500.00 ),
    (6, 'Komal', 22, 'Hyderabad', 4500.00 ),
    (7, 'Muffy', 24, 'Indore', 10000.00 );
```

Let us say we only want the data in ID, NAME and SALARY columns of the CUSTOMERS table. So, we should only specify those three columns in our SELECT statement as shown below:

```sql
SELECT ID, NAME, SALARY FROM CUSTOMERS;
```

**Output**

The output obtained is as shown below:

| ID | NAME    | SALARY  |
|----|---------|---------|
| 1  | Ramesh  | 2000.00 |
| 2  | Khilan  | 1500.00 |
| 3  | Kaushik | 2000.00 |
| 4  | Chaitali| 6500.00 |
| 5  | Hardik  | 8500.00 |
| 6  | Komal   | 4500.00 |
| 7  | Muffy   | 10000.00|

### 2. Use Wildcards
Wildcards (%) are characters that we use to search for data based on patterns. These wildcards paired with indexes only improves performance because the database can quickly find the data that matches the pattern.

**Example**

If we want to retrieve the names of all the customers starting with K from the CUSTOMERS table, then, the following query will provide the quickest result.

```sql
SELECT ID, NAME FROM CUSTOMERS WHERE NAME LIKE 'K%';
```

**Output**

Following is the output of the above query:

| ID | NAME    |
|----|---------|
| 2  | Khilan  |
| 3  | Kaushik |
| 6  | Komal   |

### 3. Use Explicit Join
SQL JOINs are used to combine two tables based on a common column. There are two ways of creating a JOIN implicit join and explicit join. Explicit Join notation use the JOIN keyword with the ON clause to join two tables while the implicit join notation does not use the JOIN keyword and works with the WHERE clause.

Performance wise, they are both on the same level. However, in more complicated cases, the implicit join notation might produce completely different results than intended. Therefore, Explicit Joining is preferred.

### 4. Avoid using SELECT DISTINCT

The DISTINCT operator in SQL is used to retrieve unique records from the database. And on a properly designed database table with unique indexes, we rarely use it.

But, if we still have to use it on a table, using the GROUP BY clause instead of the DISTINCT keyword shows a better query performance (at least in some databases).

### 5. Avoid using Multiple OR

The OR operator is used to combine multiple conditions when filtering a database. Whenever we use OR in a filter condition each statement is processed separately. This degrades database performance as the entire table must be scanned multiple times to retrieve the data that matches the filter condition.

Instead, we can use a more optimized solution; by breaking the different OR conditions into separate queries, which can be processed parallelly by the database. Then, the results from these queries can be combined using UNION.

**Example**

For example, let us say we have a requirement of getting the details of all the customers whose age is greater than 25 or whose salary is greater than 2,000. The optimized query would be as show below:

```sql
SELECT ID, NAME FROM CUSTOMERS WHERE AGE > 25 
UNION
SELECT ID, NAME FROM CUSTOMERS WHERE SALARY > 2000;
```

**Output**

After executing the above code, we get the following output:

| ID | NAME    |
|----|---------|
| 1  | Ramesh  |
| 5  | Hardik  |
| 4  | Chaitali|
| 6  | Komal   |
| 7  | Muffy   |

### 6. Use WHERE instead of HAVING

The WHERE and HAVING clause are both used to filter data in SQL. However, WHERE clause is more efficient than HAVING. With WHERE clause, only the records that match the condition are retrieved. But with HAVING clause, it first retrieves all the records and then filters them based on a condition. Therefore, the WHERE clause is preferable.

## Database Defragmentation

When the data is stored in a database, they are placed in contiguous physical locations. In this case, both logical locations and physical locations are in the same order.

However, when the database tables are altered by deleting or updating the records, indexes are also altered to suit the changes made. This will cause the indexes to be scattered across the storage. Physical locations also lose the contiguous allocation. Thus, reducing the database performance.

Defragmentation is the solution this problem. It will reorganize/rebuild the logical ordering of the indexes to match the physical ordering. But, this process first analyses the indexes and chooses whether they only need to be reorganized or rebuilt completely.

## Built-In Tuning Tools

Some databases provide built-in tuning tools to monitor the database performance. For instance, the Oracle database provides the following tuning tools:

- __EXPLAIN__ − In SQL, the EXPLAIN command give us the order in which a query is executed along with the estimated cost of each step. We can use this to find the query the least cost to optimize the database.
- __tkprof__ − tkprof is a command that gives us various statistics, such as CPU and I/O usage of a query. By using these statistics, we can tune our queries to reduce CPU and I/O utilization to increase the efficiency of our database.
