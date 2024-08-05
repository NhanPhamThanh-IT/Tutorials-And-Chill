# Transactions

Transactions group a set of tasks into a single execution unit. Each transaction begins with a specific job and ends when all the tasks in the group successfully completed. If any of the tasks fail, the transaction fails. Therefore, a transaction has only two results: **success** or **failure**.

Example of a transaction to transfer $150 from account A to account B:

> [!NOTE]
> 
>     1. read(A)
>     2. A:= A – 150
>     3. write(A)
>     4. read(B)
>     5. B:= B + 150
>     6. write(B)

Incomplete steps result in the failure of the transaction. A database transaction, by definition, must be atomic, consistent, isolated, and durable. 

These are popularly known as ACID properties.  These properties can ensure the concurrent execution of multiple transactions without conflict.

## Properties of Transaction
- **Atomicity**: The outcome of a transaction can either be completely successful or completely unsuccessful. The whole transaction must be rolled back if one part of it fails.
- **Consistency**: Transactions maintain integrity restrictions by moving the database from one valid state to another.
- **Isolation**: Concurrent transactions are isolated from one another, assuring the accuracy of the data.
- **Durability**: Once a transaction is committed, its modifications remain in effect even in the event of a system failure.

## How to Implement Transactions Control Command using SQL?
The following commands are used to control transactions. It is important to note that these statements cannot be used while creating tables and are only used with the DML Commands such as- INSERT, UPDATE, and DELETE. 

### BEGIN TRANSACTION Command
It indicates the start point of an explicit or local transaction. 

**Syntax**

> [!IMPORTANT]
> 
>     BEGIN TRANSACTION transaction_name ;

### SET TRANSACTION Command
The values for the properties of the current transaction, such as the transaction isolation level and access mode, are set using the SET TRANSACTION Statement in MySQL.

**Syntax** 

> [!IMPORTANT]
>
>     SET TRANSACTION [ READ WRITE | READ ONLY ];

### COMMIT Command
If everything is in order with all statements within a single transaction, all changes are recorded together in the database is called committed. The COMMIT command saves all the transactions to the database since the last COMMIT or ROLLBACK command. 

**Syntax**

> [!IMPORTANT]
> 
>     COMMIT;

### Example

**Sample Table1**

![OUTPUT](https://media.geeksforgeeks.org/wp-content/uploads/20230905161651/1-38.jpg)

Following is an example which would delete those records from the table which have age = 20 and then COMMIT the changes in the database. 

**Query**

> [!IMPORTANT]
>
>     DELETE FROM Student WHERE AGE = 20;
>     COMMIT;

**Output**
Thus, two rows from the table would be deleted and the SELECT statement would look like, 

![OUTPUT](https://media.geeksforgeeks.org/wp-content/uploads/20230905161804/2-34.jpg)

### ROLLBACK Command
If any error occurs with any of the SQL grouped statements, all changes need to be aborted. The process of reversing changes is called rollback. This command can only be used to undo transactions since the last COMMIT or ROLLBACK command was issued. 

**Syntax for ROLLBACK command** 

> [!IMPORTANT]
>
>     ROLLBACK;

**Example**

From the above example Sample table1, delete those records from the table which have age = 20 and then ROLLBACK the changes in the database. 

**Query**

> [!IMPORTANT]
>
>     DELETE FROM Student WHERE AGE = 20;
>     ROLLBACK;

**Output**

![OUTPUT](https://media.geeksforgeeks.org/wp-content/uploads/20230906121451/3-23.jpg)

### SAVEPOINT Command
**SAVEPOINT** creates points within the groups of transactions in which to ROLLBACK. 

A SAVEPOINT is a point in a transaction in which you can roll the transaction back to a certain point without rolling back the entire transaction. 

**Syntax for Savepoint command**

> [!IMPORTANT]
> 
>     SAVEPOINT SAVEPOINT_NAME;

This command is used only in the creation of SAVEPOINT among all the transactions. 

In general ROLLBACK is used to undo a group of transactions. 

**Syntax for rolling back to Savepoint Command**

> [!IMPORTANT]
>
>     ROLLBACK TO SAVEPOINT_NAME;

You can ROLLBACK to any SAVEPOINT at any time to return the appropriate data to its original state.

**Example**

From the above example Sample table1, Delete those records from the table which have age = 20 and then ROLLBACK the changes in the database by keeping Savepoints. 

**Query**

> [!IMPORTANT]
>
>     SAVEPOINT SP1;
>     //Savepoint created.
>     DELETE FROM Student WHERE AGE = 20;
>     //deleted
>     SAVEPOINT SP2;
>     //Savepoint created.

Here SP1 is first SAVEPOINT created before deletion.In this example one deletion have taken place. 

After deletion again SAVEPOINT SP2 is created.

**Output**

![OUTPUT](https://media.geeksforgeeks.org/wp-content/uploads/20230905162010/4-13.jpg)

Deletion have been taken place, let us assume that you have changed your mind and decided to ROLLBACK to the SAVEPOINT that you identified as SP1 which is before deletion. 

Deletion is undone by this statement.

**Query**

> [!IMPORTANT]
>
>     ROLLBACK TO SP1;
>     //Rollback completed

**Output**

![OUTPUT](https://media.geeksforgeeks.org/wp-content/uploads/20230905162125/5-13.jpg)

### RELEASE SAVEPOINT Command
This command is used to remove a SAVEPOINT that you have created.

**Syntax**

> [!IMPORTANT]
>
>     RELEASE SAVEPOINT SAVEPOINT_NAME

Once a SAVEPOINT has been released, you can no longer use the ROLLBACK command to undo transactions performed since the last SAVEPOINT.

It is used to initiate a database transaction and used to specify characteristics of the transaction that follows. 

## Conclusion
- SQL statements are grouped together using transactions.
- They promise that either all changes are made or none at all.
- Reliability is ensured by the ACID qualities of atomicity, consistency, isolation, and durability.
- Start a transaction with “BEGIN TRANSACTION,” and finish it with “COMMIT” or “ROLLBACK” to complete or undo changes.
