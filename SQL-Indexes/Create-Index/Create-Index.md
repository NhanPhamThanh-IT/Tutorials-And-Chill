<div style='text-indent: 0 cm; background-color: white; color: black; padding-top: 20px; padding-bottom: 10px;'>

# <span style='display: flex; justify-content: center; color: #E54646'><b>CREATE INDEX Statement</b></span>

<div align='justify'>
<blockquote style='background-color: white; color: black'>

<p>SQL <strong>CREATE INDEX</strong> statement creates indexes in a table for fast and efficient data retrieval.</p>

## <span><b>CREATE INDEX Statement</b></span>

<p>The <strong>CREATE INDEX Statement in SQL</strong> is used to create indexes in tables and retrieve data from the database faster than usual.</p>

<p>Indexes are invisible structures that work behind the scenes to speed up data retrieval operations in databases. They are essential for optimizing query performance and improving overall system efficiency.</p>

<p>Indexes can not be seen by users, and are only used to speed up the process of searches/queries.</p>

### <span style='color: #BD6B09'><strong>Important Points</strong></span>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li></strong>Only use <strong>INDEX constraint</strong> on a column that is frequently searched or used in <strong>WHERE clauses</strong> of <strong>SELECT queries</strong>.</li>
      <li>Adding Indexes to all columns makes the process of updating the database slower, as on each update Index updates as well.</li>
    </td>
  </tr>
</table>

## <span><b>Syntax</b></span>

<p>There are <strong>two syntaxes</strong> to create index in table:</p>

### <span style='color: #BD6B09'><strong>CREATE INDEX Syntax</strong></span>

<p>Simple CREATE INDEX Syntax is:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE INDEX</span> <span style='color: #000000'>index_name</span>
        <br>
        <span style='color: #BD6B09'>ON</span> <span style='color: #000000'>table</span> (<span style='color: #000000'>column1</span>, <span style='color: #000000'>column2</span>…);
      </strong>
    </td>
  </tr>
</table>

<p>This will create an index on the table and duplicate values are allowed.</p>

### <span style='color: #BD6B09'><strong>CREATE UNIQUE INDEX Syntax</strong></span>

<p>CREATE UNIQUE INDEX syntax is:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE UNIQUE INDEX</span> <span style='color: #000000'>index_name</span>
        <br>
        <span style='color: #BD6B09'>ON</span> <span style='color: #000000'>table_name</span> (<span style='color: #000000'>column1</span>, <span style='color: #000000'>column2</span>, …);
      </strong>
    </td>
  </tr>
</table>

<p>This will create a unique index on the table and will not allow duplicate values.</p>

## <span><b>SQL CREATE INDEX Statement Example</b></span>

<p>Let’s look at some examples of the CREATE INDEX Statement in SQL and understand it’s working.</p>

<p>First, we will create a demo database and table, on which we will use the CREATE INDEX command.</p>

### <span style='color: #BD6B09'><strong>Demo SQL Database</strong></span>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE DATABASE</span> <span style='color: #000000'>GEEKSFORGEEKS</span>;
        <br>
        <span style='color: #BD6B09'>USE</span> <span style='color: #000000'>GEEKSFORGEEKS</span>;
        <br>
        <span style='color: #BD6B09'>CREATE TABLE</span> <span style='color: #000000'>STUDENTS</span>(
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>STUDENT_ID</span> <span style='color: #BD6B09'>INT</span> <span style='color: #BD6B09'>PRIMARY KEY</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>NAME</span> <span style='color: #BD6B09'>VARCHAR</span>(<span style='color: #000000'>20</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>ADDRESS</span> <span style='color: #BD6B09'>VARCHAR</span>(<span style='color: #000000'>20</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>AGE</span> <span style='color: #BD6B09'>INT</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>DOB</span> <span style='color: #BD6B09'>DATE</span>
        <br>);
        <br><span style='color: #BD6B09'>INSERT INTO</span> <span style='color: #000000'>STUDENTS</span> 
        <br><span style='color: #BD6B09'>VALUES</span>
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>1</span>, <span style='color: #000000'>'DEV SHARMA'</span>, <span style='color: #000000'>'91 ABC STREET'</span>, <span style='color: #000000'>25</span>, <span style='color: #000000'>'1991-08-19'</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>2</span>, <span style='color: #000000'>'ARYA RAJPUT'</span>, <span style='color: #000000'>'77 XYZ STREET'</span>, <span style='color: #000000'>21</span>, <span style='color: #000000'>'1999-09-29'</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>3</span>, <span style='color: #000000'>'GAURAV VERMA'</span>, <span style='color: #000000'>'101 YEMEN ROAD'</span>, <span style='color: #000000'>29</span>, <span style='color: #000000'>'2000-01-01'</span>);
      </strong>
    </td>
  </tr>
</table>

<br>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20230830011654/Screenshot-2023-08-30-011334.png' style='border: solid black 5px'><br><small><i>Inserting data</i></small></div>

### <span style='color: #BD6B09'><strong>Create Index in SQL Table Example</strong></span>

<p>In this example, we will use the CREATE INDEX command to create an index.</p>

<p><strong>Query</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE INDEX</span> <span style='color: #000000'>idx</span>
        <br><span style='color: #BD6B09'>ON</span> <span style='color: #000000'>STUDENTS</span>(<span style='color: #000000'>NAME</span>);
      </strong>
    </td>
  </tr>
</table>

<p><strong>Output</strong></p>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20230830010840/Screenshot-2023-08-30-010604.png' style='border: solid black 5px'><br><small><i>Creating an index</i></small></div>

### <span style='color: #BD6B09'><strong>Retrieving Data From the Table Using Indexes</strong></span>

<p>In this example, we will use the <strong>USE INDEX</strong> command to retrieve data from the table.</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SELECT</span> *<br>
        <span style='color: #BD6B09'>FROM</span> <span style='color: #000000'>STUDENTS</span> 
        <br><span style='color: #BD6B09'>USE INDEX</span>(<span style='color: #000000'>idx</span>);
      </strong>
    </td>
  </tr>
</table>

<p><strong>Output</strong></p>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20230830011934/Screenshot-2023-08-30-011923.png' style='border: solid black 5px'><br><small><i>Retrieving data</i></small></div>

## <span><b>Important Points About SQL CREATE INDEX Statement</b></span>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>The CREATE INDEX statement</strong> − This statement is used to create indexes in tables to retrieve data more quickly.</li>
      <li><strong>Indexes are used to improve the efficiency of searches for data</strong> − They help in presenting data in a specific order and enhance performance when joining tables.</li>
      <li><strong>Increasing the number of indexes in a database can impact overall system performance</strong> − Therefore, indexes should be created on columns that will be frequently searched to balance performance and resource usage.</li>
      <li><strong>The CREATE UNIQUE INDEX statement</strong> − This creates a unique index on a table where duplicate values are not allowed, ensuring data integrity.</li>
      <li><strong>The DROP INDEX statement</strong> − This statement is used to delete an index from a table in SQL when it is no longer needed.</li>
    </td>
  </tr>
</table>

## <span><b>SQL Create Index – FAQs</b></span>

<p><strong>Why do we need to create an index?</strong></p>
<table style='background-color: #F0F0F0'>
  <tr>
    <td style='border: solid white'>
      We create indexes for faster retrieving of data from tables.
    </td>
  </tr>
</table>

<p><strong>How do we create an index?</strong></p>
<table style='background-color: #F0F0F0'>
  <tr>
    <td style='border: solid white'>
      We create indexes using CREATE INDEX command.
    </td>
  </tr>
</table>

<p><strong>Can we add the same index in more than one column?</strong></p>
<table style='background-color: #F0F0F0'>
  <tr>
    <td style='border: solid white'>
      Yes, we can add the same index in any number of columns of the table.
    </td>
  </tr>
</table>