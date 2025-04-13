# <span style='display: flex; justify-content: center; color: #E54646'><b>SQL CREATE DATABASE</b></span>

<div align='justify'>
    <p><b>SQL CREATE DATABASE</b> statement creates a new database in SQL-based DBMS.</p>
</div>

## <span style='color: #F5A89A'><b>CREATE DATABASE In SQL</b></span>

<div align='justify'>
    <p>The <b>CREATE DATABASE</b> query in <b>SQL</b> is used to create a new database in the database management system. It is also used in <b>MySQL</b> and other relational database management systems (RDBMS) to create databases.</p>
</div>

## <span style='color: #F5A89A'><b>Syntax</b></span>

<div align='justify'>
    <p>The syntax to use the CREATE DATABASE command in SQL is:</p>
    <p style='display: flex; justify-content: center'>CREATE DATABASE database_name;</p>
<div>

## <span style='color: #F5A89A'><b>CREATE DATABASE Examples</b></span>

<div align='justify'>
    <p>Let’s look at examples of <b>how to create a database in SQL</b> and <b>how to verify database creation</b> by listing databases in the server.</p>
</div>

### <span style='color: #EC870E'><b>Creating Your First SQL Database</b></span>

<div align='justify'>
    <p>To create a new database in SQL we use the CREATE DATABASE command and then we mention the name of the database. Note that blank spaces are not allowed in the name of the database, we can only use underscore (_).</p>
    <p>As an example, we will create a new database with the name “GeeksForGeeks”.</p>
</div>

#### <span style='color: #945305'><b>SQL Query</b></span>

<div align='center'>
    <pre><code><b><strong>CREATE DATABASE</strong></b> GeeksForGeeks;<br/></code></pre>
</div>

### <span style='color: #EC870E'><b>List Databases In SQL</b></span>

<div align='justify'>
    <p>Now we will verify whether the new database that we have just created has been successfully added to our system or not.</p>
    <p>We use the <b>SHOW DATABASES</b> command and it will return a list of databases that exist in our system. Now we will look for the name of the database (GeeksForGeeks) that we have just created.</p>
</div>

#### <span style='color: #945305'><b>SQL Query In MySQL</b></span>

<div align='center'>
    <pre><code><b><strong>SHOW DATABASES;</strong></b><br/></code></pre>
</div>

#### <span style='color: #945305'><b>SQL Query In Microsoft SQL Server (T-SQL)</b></span>

<div align='center'>
    <pre><code><b><strong>SELECT</strong></b> name <b><strong>FROM</strong></b> sys.databases;<br/></code></pre>
</div>

#### <span style='color: #945305'><b>SQL Query In Oracle</b></span>

<div align='center'>
    <pre><code><b><strong>SELECT</strong></b> name <b><strong>FROM</strong></b> v$database;<br/></code></pre>
</div>

<div align='justify'>
    <p>As we can see the SHOW DATABASE command returned the list of all databases that exist in our system and in that list, the name of the database (GeeksForGeeks) that we have just created has also been added which verifies that the database has been successfully created.</p>
</div>

### <span style='color: #EC870E'><b>USE Database In SQL</b></span>

<div align='justify'>
    <p>To use a specific database in SQL, we use the <b>USE Statement</b>.</p>
</div>

#### <span style='color: #945305'><b>Syntax</b></span>

<div align='center'>
    <p>The syntax to use a database in SQL is:</p>
</div>

<div align='center'>
    <pre><code><b><strong>USE</strong></b> database_name<br/></code></pre>
</div>

## <span style='color: #F5A89A'><b>Important Points About SQL CREATE DATABASE</b></span>

<div align='justify'>

+ A <b>CREATE DATABASE</b> statement is used to create a database.
+ A database consists of tables and inside the tables, we store the data.
+ The database name is case-insensitive, so we need to create a unique database name.
+ Keep the limit of database names to <b>128 characters</b>.

</div>
