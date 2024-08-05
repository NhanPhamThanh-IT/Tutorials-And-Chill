# Subquery
In SQL a Subquery can be simply defined as a query within another query. In other words we can say that a Subquery is a query that is embedded in WHERE clause of another SQL query. Important rules for Subqueries:

- You can place the Subquery in a number of SQL clauses: WHERE clause, HAVING clause, FROM clause. Subqueries can be used with SELECT, UPDATE, INSERT, DELETE statements along with expression operator. It could be equality operator or comparison operator such as =, >, =, <= and Like operator.
- A subquery is a query within another query. The outer query is called as **main query** and inner query is called as **subquery**.
- The subquery generally executes first when the subquery doesn’t have any **co-relation** with the **main query**, when there is a co-relation the parser takes the decision **on the fly** on which query to execute on **precedence** and uses the output of the subquery accordingly.
- Subquery must be enclosed in parentheses.
- Subqueries are on the right side of the comparison operator.
- Use single-row operators with single row Subqueries. Use multiple-row operators with multiple-row Subqueries.

**Syntax**: There is not any general syntax for Subqueries. However, Subqueries are seen to be used most frequently with SELECT statement as shown below:

> [!IMPORTANT]
>
>     SELECT column_name
>     FROM table_name
>     WHERE column_name expression operator 
>         (SELECT column_name FROM table_name WHERE ...);

### Example tables

**Database**

| NAME    | ROLL_NO | LOCATION    | PHONE_NUMBER |
|---------|---------|-------------|--------------|
| Ram     | 101     | Chennai     | 9988775566   |
| Raj     | 102     | Coimbatore  | 8877665544   |
| Sasi    | 103     | Madurai     | 7766553344   |
| Ravi    | 104     | Salem       | 8989898989   |
| Sumathi | 105     | Kanchipuram | 8989856868   |

**Student**

| NAME    | ROLL_NO | SECTION |
|---------|---------|---------|
| Ravi    | 104     | A       |
| Sumathi | 105     | B       |
| Raj     | 102     | A       |

### Sample Queries

- To display NAME, LOCATION, PHONE_NUMBER of the students from DATABASE table whose section is A.

> [!IMPORTANT]
> 
>     SELECT NAME, LOCATION, PHONE_NUMBER 
>     FROM DATABASE 
>     WHERE ROLL_NO IN (SELECT ROLL_NO 
>                       FROM STUDENT 
>                       WHERE SECTION='A');

- **Explanation**: First subquery executes “ SELECT ROLL_NO from STUDENT where SECTION=’A’ ” returns ROLL_NO from STUDENT table whose SECTION is ‘A’.Then outer-query executes it and return the NAME, LOCATION, PHONE_NUMBER from the DATABASE table of the student whose ROLL_NO is returned from inner subquery.

| NAME | ROLL_NO | LOCATION    | PHONE_NUMBER |
|------|---------|-------------|--------------|
| Ravi | 104     | Salem       | 8989898989   |
| Raj  | 102     | Coimbatore  | 8877665544   |

- Insert query example

| NAME | ROLL_NO | LOCATION    | PHONE_NUMBER |
|------|---------|-------------|--------------|
| Ram  | 101     | chennai     | 9988773344   |
| Raju | 102     | coimbatore  | 9090909090   |
| Ravi | 103     | salem       | 8989898989   |

| NAME | ROLL_NO | LOCATION    | PHONE_NUMBER |
|------|---------|-------------|--------------|
| Raj  | 111     | chennai     | 8787878787   |
| Sai  | 112     | mumbai      | 6565656565   |
| Sri  | 113     | coimbatore  | 7878787878   |

- To insert Student - 2 into Student - 1 table

> [!IMPORTANT]
>
>     INSERT INTO Student1 
>     SELECT * FROM Student2;

- **Output**

| NAME | ROLL_NO | LOCATION    | PHONE_NUMBER |
|------|---------|-------------|--------------|
| Ram  | 101     | chennai     | 9988773344   |
| Raju | 102     | coimbatore  | 9090909090   |
| Ravi | 103     | salem       | 8989898989   |
| Raj  | 111     | chennai     | 8787878787   |
| Sai  | 112     | mumbai      | 6565656565   |
| Sri  | 113     | coimbatore  | 7878787878   |

- To delete students from Student2 table whose rollno is same as that in Student1 table and having location as chennai.

> [!IMPORTANT]
> 
>     DELETE FROM Student2 
>     WHERE ROLL_NO IN (SELECT ROLL_NO 
>                       FROM Student1 
>                       WHERE LOCATION = 'chennai');

**Output**

> [!IMPORTANT]
>
>     1 row delete successfully.

- Display Student2 table

| NAME | ROLL_NO | LOCATION    | PHONE_NUMBER |
|------|---------|-------------|--------------|
| Sai  | 112     | mumbai      | 6565656565   |
| Sri  | 113     | coimbatore  | 7878787878   |

- To update name of the students to geeks in Student2 table whose location is same as Raju,Ravi in Student1 table.

> [!IMPORTANT]
> 
>     UPDATE Student2 
>     SET NAME='geeks' 
>     WHERE LOCATION IN (SELECT LOCATION 
>                        FROM Student1 
>                        WHERE NAME IN ('Raju', 'Ravi'));

**Output**

> [!IMPORTANT]
>
>     1 row updated successfully.

- Display Student2 table

| NAME  | ROLL_NO | LOCATION    | PHONE_NUMBER |
|-------|---------|-------------|--------------|
| Sai   | 112     | mumbai      | 6565656565   |
| geeks | 113     | coimbatore  | 7878787878   |
