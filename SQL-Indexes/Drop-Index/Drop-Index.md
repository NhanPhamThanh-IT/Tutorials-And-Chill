<div style='text-indent: 0 cm; background-color: white; color: black; padding-top: 20px; padding-bottom: 10px;'>

# <span style='display: flex; justify-content: center; color: #E54646'><b>DROP INDEX Statement</b></span>

<div align='justify'>
<blockquote style='background-color: white; color: black'>

<p>The <strong>SQL DROP INDEX statement removes an existing Index</strong> from a database table.</p>

## <span><b>SQL DROP INDEX</b></span>

<p>The <strong>SQL DROP INDEX Command</strong> is used to remove an index from the table. Indexes occupy space, which can cause extra time consumption on table modification operations.</p>

### <span style='color: #A0522D'><strong>Benefits of Using DROP INDEX</strong></span>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>Removing unused indexes can improve INSERT, UPDATE, and DELETE operations on the table</strong> − Unused indexes can slow down data modification operations, so removing them can enhance performance.</li>
      <li><strong>It will also free up some space</strong> − Unused indexes consume storage space, and removing them helps to reclaim that space.</li>
      <li><strong>Deleting an index can have a significant impact on database queries</strong> − Be cautious when dropping indexes, as it can affect query performance. Only drop indexes that are confirmed to be unused or unnecessary.</li>
    </td>
  </tr>
</table>

<br>

<table style='background-color: #FFE4B5'>
  <tr>
    <td style='border: solid white'>
      <strong>Note</strong>: Indexes created by <strong>PRIMARY KEY</strong> or <strong>UNIQUE constraint</strong> can not be deleted with just a <strong>DROP INDEX statement</strong>. To delete such indexes, we need to first drop the constraints using the <strong>ALTER TABLE</strong> statement, and then drop the index.
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>Syntax</strong></span>

<p>DROP INDEX Syntax differs in different database systems.</p>

<p><strong>MySQL</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #ECAB53'>ALTER TABLE</span> <span style='color: #000000'>table_name</span> 
        <br><span style='color: #ECAB53'>DROP INDEX</span> <span style='color: #000000'>index_name</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>MS Access</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #ECAB53'>DROP INDEX</span> <span style='color: #000000'>index_name</span> 
        <br><span style='color: #ECAB53'>ON</span> <span style='color: #000000'>table_name</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>SQL Server</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #ECAB53'>DROP INDEX</span> <span style='color: #000000'>table_name.index_name</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>DB2/Oracle</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #ECAB53'>DROP INDEX</span> <span style='color: #000000'>index_name</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>PostgreSQL</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #ECAB53'>DROP INDEX</span> <span style='color: #000000'>index_name</span>;
      </strong>
    </td>
  </tr>
</table>

## <span><b>SQL DROP INDEX Example</b></span>

<p>Let’s look at some examples of how to drop an index in SQL.</p>

<p>First, let’s create a table and add an index using the <strong>CREATE INDEX Statement</strong>. We will be using SQL database in the examples.</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #ECAB53'>CREATE DATABASE</span> <span style='color: #000000'>GEEKSFORGEEKS</span>;
        <br>
        <span style='color: #ECAB53'>USE</span> <span style='color: #000000'>GEEKSFORGEEKS</span>;
        <br><br>
        <span style='color: #ECAB53'>CREATE TABLE</span> <span style='color: #000000'>EMPLOYEE</span>(
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>EMP_ID</span> <span style='color: #BD6B09'>INT</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>EMP_NAME</span> <span style='color: #BD6B09'>VARCHAR</span>(<span style='color: #000000'>20</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>AGE</span> <span style='color: #BD6B09'>INT</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>DOB</span> <span style='color: #BD6B09'>DATE</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>SALARY</span> <span style='color: #BD6B09'>DECIMAL</span>(<span style='color: #000000'>7</span>,<span style='color: #000000'>2</span>)
        <br>);
        <br>
        <span style='color: #ECAB53'>CREATE INDEX</span> <span style='color: #000000'>EMP</span>
        <br><span style='color: #ECAB53'>ON</span> <span style='color: #000000'>EMPLOYEE</span>(<span style='color: #000000'>EMP_ID</span>, <span style='color: #000000'>EMP_NAME</span>);
      </strong>
    </td>
  </tr>
</table>

<p><strong>Output</strong></p>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20230830015811/Screenshot-2023-08-30-015717.png' style='border: solid black 5px'><br><small><i>Creating an index on two columns</i></small></div>

<p>Now let’s look at some examples of DROP INDEX statement and understand its workings in SQL. We will learn different use cases of the SQL DROP INDEX statement with examples.</p>

<p>We can drop the index using two ways either with <strong>IF EXISTS</strong> or with <strong>ALTER TABLE</strong> so we will first drop the index using if exists.</p>

### <span style='color: #A0522D'><strong>SQL DROP INDEX with IF EXISTS Example</strong></span>

<p>Removing an index using SQL DROP INDEX statement with <strong>IF EXISTS clause</strong>, allows the user to remove the index only if it exists in the table.</p>

<p><strong>Query</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #ECAB53'>DROP INDEX IF EXISTS</span> <span style='color: #000000'>EMP</span> 
        <br><span style='color: #ECAB53'>ON</span> <span style='color: #000000'>EMPLOYEE</span>;
      </strong>
    </td>
  </tr>
</table>

<br>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20230913193920/Screenshot-2023-09-13-193831.png' style='border: solid black 5px'><br><small><i>Dropping index</i></small></div>

<p><strong>Output</strong></p>

<p>Since there are no indexes in the database with the supplied name, the aforementioned query simply ends execution without returning any errors.</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>Commands Executed Successfully;</strong>
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>SQL DROP index with ALTER TABLE Example</strong></span>

<p><strong>Query</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #ECAB53'>ALTER TABLE</span> <span style='color: #000000'>EMPLOYEE</span>
        <br><span style='color: #ECAB53'>DROP INDEX</span> <span style='color: #000000'>EMP</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>Output</strong></p>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20230830020053/Screenshot-2023-08-30-020024.png' style='border: solid black 5px'><br><small><i>Dropping the index</i></small></div>

## <span><b>Verify DROP INDEX</b></span>

<p>To verify if the DROP INDEX statement has successfully removed the index from the table, we can check the indexes on the table. If the index is not present in the list, we know it has been deleted.</p>

### <span style='color: #A0522D'><strong>Syntax</strong></span>

<p>The syntax for viewing the index on a table differs for different databases, for example:</p>

<p><strong>SQL Server</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SELECT</span> * 
        <span style='color: #BD6B09'>FROM</span> sys.indexes 
        <span style='color: #BD6B09'>WHERE</span> object_id = 
        <span style='color: #BD6B09'>(</span>
          <span style='color: #BD6B09'>SELECT</span> object_id 
          <span style='color: #BD6B09'>FROM</span> sys.objects 
          <span style='color: #BD6B09'>WHERE</span> name = <span style='color: #000000'>'YOUR_TABLE_NAME'</span>
        <span style='color: #BD6B09'>)</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>MySQL</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SHOW INDEXES</span> 
        <span style='color: #BD6B09'>FROM</span> <span style='color: #000000'>YOUR_TABLE_NAME</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>PostgreSQL</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SELECT</span> * 
        <span style='color: #BD6B09'>FROM</span> <span style='color: #000000'>USER_INDEXES</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>Oracle</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SELECT</span> <span style='color: #000000'>indexname</span>, <span style='color: #000000'>indexdef</span> 
        <span style='color: #BD6B09'>FROM</span> <span style='color: #000000'>pg_indexes</span> 
        <span style='color: #BD6B09'>WHERE</span> <span style='color: #000000'>tablename</span> = <span style='color: #000000'>'your_table_name'</span>;
      </strong>
    </td>
  </tr>
</table>

## <span><b>Important Points About SQL DROP INDEX Statement</b></span>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>The SQL DROP INDEX statement</strong> − This statement is used to remove an existing index from a database table.</li>
      <li><strong>It optimizes database performance by reducing index maintenance overhead</strong> − Removing unnecessary indexes reduces the overhead of maintaining indexes, which can improve overall database performance.</li>
      <li><strong>It improves the speed of INSERT, UPDATE, and DELETE operations on the table</strong> − Dropping unused indexes can enhance the speed of data modification operations by reducing the maintenance burden on the database.</li>
      <li><strong>Indexes created by PRIMARY KEY or UNIQUE constraints cannot be dropped using just the DROP INDEX statement</strong> − These indexes are integral to the table’s structure and must be managed through other statements or constraints.</li>
      <li><strong>The IF EXISTS clause can be used to conditionally drop the index only if it exists</strong> − This clause prevents errors by ensuring that the index is dropped only if it is present.</li>
      <li><strong>To verify if the DROP INDEX statement has successfully removed the index from the table</strong> − Check the list of indexes on the table to confirm the removal.</li>
    </td>
  </tr>
</table>

## <span><b>SQL DROP INDEX Statement – FAQs</b></span>

<p><strong>How to create an index in SQL?</strong></p>

<table><tr style='background-color: #F0F0F0; border: solid white'><td>To create an index in MYSQL we use the CREATE INDEX command.</td></tr></table>

<p><strong>How to drop an index in SQL?</strong></p>

<table><tr style='background-color: #F0F0F0; border: solid white'><td>To drop an index in SQL we use the ALTER TABLE DROP INDEX command.</td></tr></table>

<p><strong>What is the need to drop an index?</strong></p>

<table><tr style='background-color: #F0F0F0; border: solid white'><td>Generally we drop an index and then recreate it because it increases the data insertion speed.</td></tr></table>