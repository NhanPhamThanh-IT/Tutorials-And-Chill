# CTE in SQL

The **Common Table Expressions (CTE)** were introduced into standard SQL in order to simplify various classes of SQL Queries for which a derived table was just unsuitable. CTE was introduced in SQL Server 2005, the common table expression (CTE) is a temporary named result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement. You can also use a CTE in a CREATE view, as part of the view’s SELECT query. In addition, as of SQL Server 2008, you can add a CTE to the new MERGE statement. 

## Why do We Need CTE in the SQL server?
A common table [deprecated]CTE is a powerful SQL construct that helps simplify queries. CTEs act as virtual tables (with records and columns) that are created during query execution, used by the query, and deleted after the query executes.

## Using the CTE 
We can define CTEs by adding a WITH clause directly before the SELECT, INSERT, UPDATE, DELETE, or MERGE statement. The WITH clause can include one or more CTEs separated by commas. 

**Syntax**

```sql
[WITH  [, …]]  
::=
cte_name [(column_name [, …])]
AS (cte_query)
```

**Argument**

1. __Expression name__: A valid identifier for a common table expression. The expression_name must be different from the names of other common table expressions defined in the same WITH  clause, but the expression_name can be the same as the name of the base table or view. All references to expression_name in the query use the common table expression instead of the base object.
2. __Column name__: Specifies a column name in a common table expression. Duplicate names within a single CTE definition are not allowed. The number of column names must match the number of columns in the CTE_query_definition’s result set. A list of column names is optional only if all the resulting columns in the query definition have different names.
3. __CTE_QueryDefinition__: Specifies a SELECT statement whose result set satisfies a common table expression. The SELECT statement for CTE_query_defining must meet the same requirements as creating a view, except that a CTE cannot define another CTE. For more information, see the Remarks section and CREATE VIEW (Transact-SQL). If multiple CTE_query_settings are defined, the query definitions must be combined with one of the set operators UNION ALL, UNION, EXCEPT, or INTERSECT.

## Rules for Define and Use of Recursive Common Table Expressions

The following guidelines apply to defining recursive common table expressions:

1. A recursive CTE definition must contain at least two he CTE query definitions, an anchor member and a recursive member. You can define multiple anchor and recursive members. However, all anchor member query definitions must be placed before the first recursive member definition. All CTE query definitions are anchor members unless they reference the CTE itself.
2. Anchor elements must be combined with one of the following set operators: UNION ALL, UNION, INTERSECT, EXCEPT. UNION ALL is the only valid set operator between the last anchor member and the first recursive member when joining multiple recursive members. Anchor and recursive elements must have the same number of columns.
3. The data type of the recursive member’s columns must be the same as the data type of the corresponding column of the anchor member.
4. The following items are not allowed in her CTE_query_definition for recursive members:

> [!IMPORTANT]
>
>     Please choose a different grouping
>     PIVOT (For database compatibility level 110 and above. 
>     See Breaking Changes to Database Engine Features in SQL Server 2016.
>     Offal Scalar aggregation Up
>     LEFT, RIGHT, OUTER JOIN (INNER JOIN is allowed)
>     subquery
>     A hint applied to recursive references to CTEs within a CTE_query_definition.

## Creating a Recursive Common Table Expression

A recursive CTE is one that references itself within that CTE. The recursive CTE is useful when working with hierarchical data as the CTE continues to execute until the query returns the entire hierarchy. 

A typical example of hierarchical data is a table that includes a list of employees. For every employee, the table provides a reference to that person’s manager. That reference is itself an employee ID within the same table. You can use a recursive CTE to display the hierarchy of employee data. 

If a CTE is created incorrectly it can enter an infinite loop. To prevent this, the MAXRECURSION hint can be added in the OPTION clause of the primary SELECT, INSERT, UPDATE, DELETE, or MERGE statement. 

**A table is created**

```sql
CREATE TABLE Employees
(
    EmployeeID int NOT NULL PRIMARY KEY,
    FirstName varchar(50) NOT NULL,
    LastName varchar(50) NOT NULL,
    ManagerID int NULL
)

INSERT INTO Employees VALUES (1, 'Ken', 'Thompson', NULL)
INSERT INTO Employees VALUES (2, 'Terri', 'Ryan', 1)
INSERT INTO Employees VALUES (3, 'Robert', 'Durello', 1)
INSERT INTO Employees VALUES (4, 'Rob', 'Bailey', 2)
INSERT INTO Employees VALUES (5, 'Kent', 'Erickson', 2)
INSERT INTO Employees VALUES (6, 'Bill', 'Goldberg', 3)
INSERT INTO Employees VALUES (7, 'Ryan', 'Miller', 3)
INSERT INTO Employees VALUES (8, 'Dane', 'Mark', 5)
INSERT INTO Employees VALUES (9, 'Charles', 'Matthew', 6)
INSERT INTO Employees VALUES (10, 'Michael', 'Jhonson', 6)
```

After the Employees table is created, the following SELECT statement, which is preceded by a WITH clause that includes a CTE named cteReports is created: 

```sql
WITH cteReports (EmpID, FirstName, LastName, MgrID, EmpLevel)
AS
(
    SELECT EmployeeID, FirstName, LastName, ManagerID, 1
    FROM Employees
    WHERE ManagerID IS NULL
    UNION ALL
    SELECT e.EmployeeID, e.FirstName, e.LastName, e.ManagerID, r.EmpLevel + 1
    FROM Employees e
        INNER JOIN cteReports r
            ON e.ManagerID = r.EmpID
)
SELECT
  FirstName + ' ' + LastName AS FullName, EmpLevel,
  (SELECT FirstName + ' ' + LastName FROM Employees
  WHERE EmployeeID = cteReports.MgrID) AS Manager
  FROM cteReports
  ORDER BY EmpLevel, MgrID
```

Thus, CTEs can be useful when you need to generate temporary result sets that can be accessed in a SELECT, INSERT, UPDATE, DELETE, or MERGE statement.

## Features and Limitations of Common Table Expressions in Azure

The current implementation of CTEs in Azure Synapse Analytics and Analytics Platform System (PDW) has the following features and limitations:

1. A CTE can be only specified in a SELECT statement.
2. A CTE can be only specified in a CREATE VIEW statement.
3. A CTE can be only specified in a CREATE TABLE AS SELECT (CTAS) statement.
4. A CTE can be only specified in a CREATE REMOTE TABLE AS SELECT (CRTAS) statement.
5. A CTE can be only specified in a CREATE EXTERNAL TABLE AS SELECT (CETAS) statement.
