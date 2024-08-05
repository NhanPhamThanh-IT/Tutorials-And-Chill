<div align='justify'>

# Auto Increment

Sometimes while creating a table we do not have a unique identifier within the table hence we face difficulty in choosing the Primary Key. So as to resolve such an issue we’ve to manually provide unique keys to every record but this is often also a tedious task. So we can use the Auto Increment feature that automatically generates a numerical Primary key value for every new record inserted. The Auto Increment feature is supported by all the Databases we are going to discuss the auto-increment field for the subsequent DBMS:

- SQL Server
- MySQL
- PostgreSQL
- MS Access
- Oracle

## **SQL Server Auto Incrementauto-increment**
In SQL Server, IDENTITY(starting_value, increment_value) is used for the auto-increment feature. Here,

- **starting_value** – Mention the starting value we would like to use.
- **increment_value** – Mention the value by which we would like to increment the key for the subsequent record.

**Example**: We will create a Student table with fields Student_ID, First_Name, and Last_Name, we will auto-generate Student_ID by using auto-increment and will make it the Primary Key for the table. Let the starting value of IDENTITY be 101 and we will increment the auto-generated key by 1 for each new record.

```SQL
CREATE TABLE Students(
    Student_ID int IDENTITY(101, 1) PRIMARY KEY, 
    First_Name varchar(255),
    Last_Name varchar(255)
);
```

To insert a new record into students table, we will not specify the value of Student_ID as it will be added automatically.

```SQL
INSERT INTO Students(First_Name, Last_Name) 
VALUES ('Deeksha', 'Jain');
     
INSERT INTO Students(First_Name, Last_Name) 
VALUES ('Kavisha', 'Parikh');
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200515125215/article-table.png)

## **MySQL Auto Increment**
In MySQL, AUTO_INCREMENT keyword is employed for auto increment feature. By default, the AUTO_INCREMENT starts with 1 and increases by 1. Example: We will create Students table with fields Student_ID, First_Name, Last_Name, we will auto generate Student_ID by using auto increment and will make it Primary Key for the table.

```SQL
CREATE TABLE Students(
    Student_ID int AUTO_INCREMENT PRIMARY KEY, 
    First_Name varchar(255),
    Last_Name varchar(255)
);
```

To insert a new record into students table, we will not specify the value of Student_ID as it will be added automatically and the first record will have key as 1 and key for every subsequent record will increase by 1.

```SQL
INSERT INTO Students(First_Name, Last_Name) 
VALUES ('Anish', 'Jain');
     
INSERT INTO Students(First_Name, Last_Name) 
VALUES ('Akshita', 'Sharma');
     
INSERT INTO Students(First_Name, Last_Name) 
VALUES ('Shruti', 'Sogani');
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200515141439/article-table1.png)

To change the default starting value we can use ALTER TABLE command as follows:

```sql
ALTER TABLE Students AUTO_INCREMENT = new_value;
```

Here new_value is that the starting value we would like to use. To change the AUTO_INCREMENT interval value to a number different from 1, we assign new interval value to MySQL Server’s variable auto_increment_increment.

>
> mysql>
> SET @@ auto_increment_increment=new_interval_value;

Here new_interval_value is the interval value we would like to use.

## **PostgreSQL Auto Increment**
In PostgreSQL, SERIAL keyword is used for auto increment feature. Example: We will create Students table with fields Student_ID, First_Name, Last_Name, we will auto generate Student_ID by using auto increment and will make it Primary Key for the table.

```SQL
CREATE TABLE Students(
      Student_ID int SERIAL PRIMARY KEY, 
      First_Name varchar(255),
      Last_Name varchar(255)
); 
```

To insert a new record into students table, we will not specify the value of Student_ID as it will be added automatically.

```SQL
INSERT INTO Students(First_Name, Last_Name ) 
VALUES ('Anish', 'Jain');

INSERT INTO Students(First_Name, Last_Name ) 
VALUES ('Akshita', 'Sharma');

INSERT INTO Students(First_Name, Last_Name ) 
VALUES ('Shruti', 'Sogani'); 
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200515141439/article-table1.png)

## **MS Access Auto Increment** 
In MS Access, AUTOINCREMENT keyword is used to perform an auto-increment feature. By default, the AUTOINCREMENT starts with 1 and increases by 1.

**Example**: We will create Students table with fields Student_ID, First_Name, Last_Name, we will auto generate Student_ID by using auto increment and will make it Primary Key for the table.

```SQL
CREATE TABLE Students(
      Student_ID int AUTOINCREMENT PRIMARY KEY, 
      First_Name varchar(255),
      Last_Name varchar(255)
); 
```

To insert a new record into students table, we will not specify the value of Student_ID as it will be added automatically and the first record will have key as 1 and key for every subsequent record will increase by 1.

```SQL
INSERT INTO Students(First_Name, Last_Name ) 
VALUES ('Anish', 'Jain');

INSERT INTO Students(First_Name, Last_Name ) 
VALUES ('Akshita', 'Sharma');

INSERT INTO Students(First_Name, Last_Name ) 
VALUES ('Shruti', 'Sogani');
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200515141439/article-table1.png)

To change the default starting value and increment value we can use AUTOINCREMENT feature as follows:

```SQL
AUTOINCREMENT(starting_value, increment_value)
```

Here starting_value is that the starting value we would like to use and increment_value is that value by which we would like to increment the key for the subsequent record.

## **Oracle Auto Increment**
In Oracle, to use auto increment feature we have to make the auto-increment field with the sequence object which successively generates a number sequence.

**Syntax**

```SQL
CREATE SEQUENCE sequence_name
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 10;
```

In the above syntax:

- **sequence_name** – It refers to the name of sequence object we would like to produce.
- **START WITH** – Followed by the starting value that we would like to use.Here we have provided 1 as starting value.
- **INCREMENT BY** – Followed by the value by which you want to increment.Here we want to increase the subsequent keys by 1.
- **CACHE** – Followed by the maximum number of values to be stored for faster access.

**Example**: The code below creates a sequence object called seq_students, that starts with 101 and can increment by 1. It’ll also cache up to 20 values for performance.

```SQL
CREATE SEQUENCE seq_students
      MINVALUE 1
      START WITH 101
      INCREMENT BY 1
      CACHE 20;
```

To insert a new record into the “Students” table, we will have to use the nextval function that retrieves the next value from seq_students sequence:

```SQL
INSERT INTO Students(Student_ID, First_Name, Last_Name)
VALUES (seq_students.nextval, 'Deeksha', 'Jain');

INSERT INTO Students(Student_ID, First_Name, Last_Name)
VALUES (seq_students.nextval, 'Kavisha', 'Parikh'); 
```

**Output**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200515125215/article-table.png)

</div>