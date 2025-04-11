# PERFORMANCE TUNING

**SQL Performance tuning** is the process of enhancing SQL queries to speed up the server performance. Performance tuning in SQL shortens the time it takes for a user to receive a response after sending a query and utilizes fewer resources in the process. The idea is that users can occasionally produce the same intended result set with a faster-running query.

<code>SQL performance tuning is speeding up queries against a relational database.</code>

It is a very important concept if you are pursuing SQL as your career. Many companies ask about SQL performance tuning in interview questions, as optimizing database speed is a priority for everyone.
In this article, we discuss various tools and techniques to increase SQL performance and learn each technique step by step.

## Table of Content
- Factors Affecting SQL Speed
- Ways to Find Slow SQL Queries in SQL Server
- Performance Tuning in SQL Query
- Index Tuning
- SQL Performance Tuning Tools

## Factors Affecting SQL Speed
Some of the major factors that influence the computation and execution time in SQL are:
- **Table size**: Performance may be impacted if your query hits one or more tables with millions of rows or more.
- **Joins**: Your query is likely to be slow if it joins two tables in a way that significantly raises the number of rows in the return set.
- **Aggregations**: Adding several rows together to create a single result needs more processing than just retrieving those values individually.
- **Other users executing queries**: The more queries a database has open at once, the more it must process at once, and the slower it will all be. It can be particularly problematic if other users are using a lot of resources to perform queries that meet some of the aforementioned requirements.

## Ways to Find Slow SQL Queries in SQL Server

**1. Create an Execution Plan**: It is essential to be able to create execution plans, which you can accomplish with SQL Server Management Studio, in order to diagnose delayed queries. After the queries run, actual execution plans are generated. To create an execution plan:
- Start by selecting “Database Engine Query” from the toolbar of SQL Server Management Studio.
- Enter the query after that, and then select “Include Actual Execution Plan” from the Query option.
- It’s time to run your query at this point. You can do that by pressing F5 or the “Execute” toolbar button.
- The execution plan will then be shown in the results pane, under the “Execution Pane” tab, in SQL Server Management Studio.

**2. Monitor Resource Usage**: The performance of a SQL database is greatly influenced by resource use. Monitoring resource use is important since you can’t improve what you don’t measure. Use the System Monitor tool on Windows to evaluate SQL Server’s performance. You may view SQL Server objects, performance counters, and other object activity with it. Simultaneously watch Windows and SQL Server counters with System Monitor to see if there is any correlation between the two services’ performance.

**3. Use SQL DMVs to Find Slow Queries**: The abundance of dynamic management views (DMVs) that SQL Server includes is one of its best features. There are many of them, and they may offer a lot of knowledge on a variety of subjects.
Various DMVs are available that offer information on query stats, execution plans, recent queries, and much more. These can be combined to offer some incredible insights.

## Performance Tuning in SQL Query
If a query is inefficient or contains errors, it will consume up the production database’s resources and slow down or disconnect other users. You must optimize your queries to have the least possible negative influence on database performance.

We have discussed few methods of **performance tuning in SQL query with examples**. The following techniques can be used to optimize SQL queries:

1. SELECT fields instead of using SELECT *
2. Avoid SELECT DISTINCT
3. Create queries with INNER JOIN (not WHERE or cross join)
4. Use WHERE instead of HAVING to define filters
5. Use wildcards at the end of a phrase only
6. Use LIMIT to sample query results
7. Run your query during off-peak hours

Let’s discuss each of these methods, and see how to use them in our database.

### SELECT fields instead of using SELECT *
Many SQL developers use the SELECT * shortcut to query all of the data in a table while executing exploratory queries. However, if a table contains a lot of fields and rows, the database would be taxed by superfluous data queries. By using the SELECT statement, one may direct the database to only query the data you actually need to suit your business needs. 

For example:

> [!NOTE]
> **Inefficient**
>  
> **Select** * **From** GeeksTable;
>
> **Efficient**
>
> **SELECT** FirstName, LastName, Address, City, State, Zip **FROM** GeeksTable;`

### Avoid SELECT DISTINCT
It is practical to get rid of duplicates from a query by using SELECT DISTINCT. To get separate results, SELECT DISTINCT GROUPs for every field in the query. However, a lot of computing power is needed to achieve this goal. Furthermore, data may be inaccurately classified to a certain extent. Choose more fields to produce distinct results instead of using SELECT DISTINCT.

> [!NOTE]
> **Inefficient and inaccurate**
>
> **SELECT DISTINCT** FirstName, LastName, State **FROM** GeeksTable;
>
> **Efficient and accurate**
>
> **SELECT** FirstName, LastName, Address, City, State, Zip **FROM** GeeksTable;

### Create  queries with INNER JOIN (not WHERE or cross join)
WHERE clause joins are preferred by some SQL developers, as in the examples below:

> [!NOTE]
> **SELECT** GFG1.CustomerID, GFG1.Name, GFG1.LastSaleDate
>
> **FROM** GFG1, GFG2
>
> **WHERE** GFG1.CustomerID = GFG2.CustomerID

A Cartesian Connection, also known as a Cartesian Product or a CROSS JOIN, is produced by this kind of join. A Cartesian Join creates every conceivable combination of the variables.

If we had 1,000 customers and 1,000 in total sales in this example, the query would first produce 1,000,000 results before filtering for the 1,000 entries where CustomerID is correctly connected.

The database has performed 100 times more work than was necessary, therefore this is a wasteful use of its resources. Due to the possibility of producing billions or trillions of results, Cartesian Joins pose a particular challenge for large-scale databases.

### To prevent creating a Cartesian Join, use INNER JOIN instead

> [!NOTE]
> **SELECT** GFG1.CustomerID, GFG1.Name, GFG1.LastSaleDate
>
> **FROM** GFG1
>
> **INNER JOIN** GFG2
>
> **ON** GFG1.CustomerID = GFG2.CustomerID

The database would only generate the limited desired records where CustomerID is equal.

### Use WHERE instead of HAVING to define filters

A successful query will only retrieve the necessary records from the database. HAVING statements are computed after **WHERE** statements in accordance with the SQL Order of Operations. A WHERE statement is more effective if the goal is to filter a query based on conditions.

Assuming 500 sales were made in 2019, for instance, query to find how many sales were made per client that year.

> [!NOTE]
> **SELECT** GFG1.CustomerID, GFG1.Name, GFG1.LastSaleDate
>
> **FROM** GFG1
>
> **INNER JOIN** GFG2
>
> **ON** GFG1.CustomerID = GFG2.CustomerID
>
> **GROUP BY** GFG1.CustomerID, GFG1.Name
>
> **HAVING** GFG2.LastSaleDate **BETWEEN** "1/1/2019" **AND** "12/31/2019"

The GFG2 table would be queried to retrieve 1,000 sales records, which would then be filtered to only include the 500 entries produced in 2019 before the dataset was counted.

WHERE clauses, in contrast, set a limit on how many records can be retrieved:

> [!NOTE]
> **SELECT** GFG1.CustomerID, GFG1.Name, GFG1.LastSaleDate
> 
> **FROM** GFG1 **INNER JOIN** GFG2
>
> **ON** GFG1.CustomerID = GFG2.CustomerID
>
> **WHERE** GFG2.LastSaleDate **BETWEEN** "1/1/2019" **AND** "12/31/2019"
>
> **GROUP BY** GFG1.CustomerID, GFG1.Name

### Use wildcards at the end of a phrase only
Wildcards enable the broadest search when searching unencrypted material, such as names or cities. However, the most extensive search is also the least effective. The database is required to search all records for a match anywhere inside the chosen field when a leading wildcard is used, particularly when combined with an ending wildcard.

Think about using this search and find cities that start with “No”:

> [!NOTE]
> **SELECT** City **FROM** GeekTable **WHERE** City **LIKE** ‘%No%’

The expected results are Noida, and Noopur, which will be returned by this query. Unexpected results will also be produced.

A better inquiry would be:

> [!NOTE]
> **SELECT** City **FROM** GeekTable **WHERE** City **LIKE** ‘No%’

### Use LIMIT to sample query results
Use a LIMIT statement to check if the results will be pleasing and useful before executing a query for the first time. (In some DBMS systems, the terms TOP and LIMIT are used synonymously.) Only the given number of records are returned by the LIMIT statement. By using a LIMIT statement, you can avoid stressing the production database with a big query only to discover that it needs to be edited or improved.

We will look at a maximum of 10 rows in the 2019 sales query from above:

> [!NOTE]
> **SELECT** GFG1.CustomerID, GFG1.Name, GFG1.LastSaleDate
>
> **FROM** GFG1
>
> **INNER JOIN** GFG2
>
> **ON** GFG1.CustomerID = GFG2.CustomerID
>
> **WHERE** GFG2.LastSaleDate **BETWEEN** "1/1/2019" **AND** "12/31/2019"
>
>  **GROUP BY** GFG1.CustomerID, GFG1.Name
>
>  **LIMIT** 10

We can see by the sample whether we have a usable data set or not.

### Run your query during off-peak hours

About planning any query to run at a time when it won’t be as busy in order to reduce the impact of your analytical queries on the database. When the number of concurrent users is at its lowest, which is often overnight, the query should be executed.

Your query should run query more frequently by using the following: 

- Selecting from large tables (>1,000,000 records)
- Cartesian Joins or CROSS JOINs
- Looping statements
- SELECT DISTINCT statements
- Nested subqueries
- Wildcard searches in long text or memo fields
- Multiple schema queries
- Query confidently

## Index Tuning
When choosing and building indexes, database tuning includes index tuning. The index tuning objective is to speed up query processing. It can be challenging to employ indexes in dynamic contexts with numerous ad-hoc searches scheduled in advance. The queries that are based on indexes are subject to index tweaking, and the indexes are generated automatically as needed. Users of the database do not need to take any specific activities to tune the index.

> Indexes can be used to increase a database’s speed and query performance. Index tuning is the process of improving the index selection.

### Advantages of Index Tuning
The performance of queries and databases can be improved by using the Index tuning wizard. It accomplishes this using the following methods:

- Recommendations for optimal index usage based on query optimizer analysis and workload
- Examination of changes in query distribution, index utilization, and performance to determine impact
- Suggestion of fine-tuning strategies for problematic queries
- Use of SQL Profiler to record activity traces and improve performance

Points to consider while creating indexes:
- Short indexes for reduced disk space and faster comparisons
- Distinct indexes with minimal duplicates for better selectivity
- Clustered indexes covering all row data for optimal performance
- Static data columns for clustered indexes to minimize shifting

Utilizing index tuning tools and following best practices is essential for maintaining high-performing SQL Server environments. Regular monitoring, proactive maintenance, and continuous improvement are key to optimizing database performance and supporting critical business applications.

## SQL Performance Tuning Tools
Here are some tools for SQL Performance Tuning:

1. SQL Sentry (SolarWinds)
2. SQL Doctor (IDERA)
3. Profiler (Microsoft)
4. SQL Defrag Manager (IDERA)
5. DB Optimizer (IDERA)
6. SQL Check (IDERA)
7. Foglight for SQL Server (Quest Software)
8. SQL Index Manager (Red Gate Software)
9. Qure Optimizer (DBSophic)
10. DBArtisan® (IDERA)
11. dbWatch Control Center (dbWatch)
12. Plan Explorer (SolarWinds / SentryOne)
13. SQL Diagnostic Manager (IDERA)
14. Database Performance Analyzer (SolarWinds)
15. Applications Manager (ManageEngine)
16. NaviCat for SQL Server (NaviCat)

## Conclusion
SQL Performance tuning is a very important aspect of database management, as it ensures efficient and optimized database operations. We have discussed various tools and techniques used to performance tuning in SQL.

Using the right performance tuning techniques, companies can ensure that their database operate at peak efficiency, supporting critical business applications and decision-making processes. As data volumes and complexity continue to grow, the importance of SQL performance tuning will only increase, making it a crucial skill for database professionals.
