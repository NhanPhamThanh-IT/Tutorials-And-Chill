<div style='text-indent: 0 cm; background-color: white; color: black; padding-top: 20px; padding-bottom: 10px;'>

# <span style='display: flex; justify-content: center; color: #E54646'><b>Unique Indexes</b></span>

<div align='justify'>
<blockquote style='background-color: white; color: black'>

### <span style='color: #A0522D'><strong>SQL Unique Indexes</strong></span>

<p>The <strong>SQL Unique Index</strong> ensures that no two rows in the indexed columns of a table have the same values (no duplicate values allowed).</p>

<p>A unique index can be created on one or more columns of a table using the CREATE UNIQUE INDEX statement in SQL.</p>

<p>Following are the points to be noted before creating a Unique Index on a table:</p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>If the unique index is only created on a single column</strong> − The rows in that column will be unique, ensuring that no duplicate values exist in the column.</li>
      <li><strong>If a single column contains NULL in multiple rows</strong> − We cannot create a unique index on that column, as NULL values are not considered equal and hence cannot enforce uniqueness.</li>
      <li><strong>If the unique index is created on multiple columns</strong> − The combination of rows in these columns will be unique, meaning that the combination of values across the specified columns must be unique.</li>
      <li><strong>We cannot create a unique index on multiple columns if the combination of columns contains NULL in more than one row</strong> − The presence of <strong>NULL</strong> in multiple rows across the indexed columns prevents enforcing uniqueness on those combinations.</li>
    </td>
  </tr>
</table>

<p><strong>Syntax</strong></p>

<p>Following is the syntax for creating a <strong>UNIQUE INDEX</strong> in SQL:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE UNIQUE INDEX</span> <span style='color: #000000'>index_name</span>
        <br><span style='color: #BD6B09'>ON</span> <span style='color: #000000'>table_name</span> 
        <br><span style='color: #BD6B09'>(</span><span style='color: #000000'>column1, column2, ..., columnN</span><span style='color: #BD6B09'>)</span>;
      </strong>
    </td>
  </tr>
</table>

<p>Here,</p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>index_name</strong> − The name of the index that you want to create.</li>
      <li><strong>table_name</strong> − The name of the table on which you want to create the index.</li>
      <li><strong>(column1, column2, ...., columnN)</strong> − The names of one or more columns on which the unique index is being created.</li>
    </td>
  </tr>
</table>

<p><strong>Example</strong></p>

<p>First of all, let us create a table named <strong>CUSTOMERS</strong> using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE TABLE</span> <span style='color: #000000'>CUSTOMERS</span>
        <br><span style='color: #BD6B09'>(</span>
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>ID</span> <span style='color: #BD6B09'>INT</span> <span style='color: #BD6B09'>NOT NULL</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>NAME</span> <span style='color: #BD6B09'>VARCHAR(15)</span> <span style='color: #BD6B09'>NOT NULL</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>AGE</span> <span style='color: #BD6B09'>INT</span> <span style='color: #BD6B09'>NOT NULL</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>ADDRESS</span> <span style='color: #BD6B09'>VARCHAR(25)</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>SALARY</span> <span style='color: #BD6B09'>DECIMAL(10, 4)</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #BD6B09'>PRIMARY KEY</span> <span style='color: #000000'>(ID)</span>
        <br><span style='color: #BD6B09'>);</span>
      </strong>
    </td>
  </tr>
</table>

<p>Insert some values into the above-created table using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>INSERT INTO</span> <span style='color: #000000'>CUSTOMERS</span> 
        <br><span style='color: #BD6B09'>VALUES</span>
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>1</span>, <span style='color: #000000'>'Ramesh'</span>, <span style='color: #000000'>'32'</span>, <span style='color: #000000'>'Ahmedabad'</span>, <span style='color: #000000'>2000</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>2</span>, <span style='color: #000000'>'Khilan'</span>, <span style='color: #000000'>'25'</span>, <span style='color: #000000'>'Delhi'</span>, <span style='color: #000000'>1500</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>3</span>, <span style='color: #000000'>'Kaushik'</span>, <span style='color: #000000'>'23'</span>, <span style='color: #000000'>'Kota'</span>, <span style='color: #000000'>2000</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>4</span>, <span style='color: #000000'>'Chaitali'</span>, <span style='color: #000000'>'26'</span>, <span style='color: #000000'>'Mumbai'</span>, <span style='color: #000000'>6500</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>5</span>, <span style='color: #000000'>'Hardik'</span>, <span style='color: #000000'>'27'</span>, <span style='color: #000000'>'Bhopal'</span>, <span style='color: #000000'>8500</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>6</span>, <span style='color: #000000'>'Komal'</span>, <span style='color: #000000'>'22'</span>, <span style='color: #000000'>'Hyderabad'</span>, <span style='color: #000000'>9000</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>7</span>, <span style='color: #000000'>'Muffy'</span>, <span style='color: #000000'>'24'</span>, <span style='color: #000000'>'Indore'</span>, <span style='color: #000000'>5500</span>);
      </strong>
    </td>
  </tr>
</table>

<p>Once the table is created, let us create a unique index for the column named <strong>SALARY</strong> in the CUSTOMERS table using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE UNIQUE INDEX</span> <span style='color: #000000'>UNIQUE_ID</span> 
        <br><span style='color: #BD6B09'>ON</span> <span style='color: #000000'>CUSTOMERS</span> 
        <br><span style='color: #BD6B09'>(<span style='color: #000000'>SALARY</span>)</span>;
      </strong>
    </td>
  </tr>
</table>

<p>But, when we execute the above query, the output is obtained as follows:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      ERROR 1062 (23000): Duplicate entry '2000.00' for key 'customers.UNIQUE_ID'
    </td>
  </tr>
</table>

<p>Since a unique index could not be created on SALARY column (due to duplicate values), let us create <strong>Unique Index</strong> on the <strong>NAME</strong> column of the same table, using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE UNIQUE INDEX</span> <span style='color: #000000'>UNIQUE_ID</span> 
        <br><span style='color: #BD6B09'>ON</span> <span style='color: #000000'>CUSTOMERS</span> 
        <br><span style='color: #BD6B09'>(<span style='color: #000000'>NAME</span>)</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>Output</strong></p>

<p>When we execute the above query, the output is obtained as follows:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <span>Query OK, 0 rows affected (0.03 sec)<br>
      Records: 0  Duplicates: 0  Warnings: 0</span>
    </td>
  </tr>
</table>

<p><strong>Verification</strong></p>

<p>Let's verify whether the unique index for the column NAME is created or not using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SHOW INDEX FROM</span> <span style='color: #000000'>CUSTOMERS</span>;
      </strong>
    </td>
  </tr>
</table>

<p>As you observe the output below, you can find the column NAME along with the ID (PRIMARY KEY) in the list of indexes.</p>

<table align='center'>
    <tr align='center' style='background-color: #F0F0F0'>
        <th>Table</th>
        <th>Non_unique</th>
        <th>Key_name</th>
        <th>Seq_in_index</th>
        <th>Column_name</th>
    </tr>
    <tr align='center'>
        <td>customers</td>
        <td>0</td>
        <td>PRIMARY</td>
        <td>1</td>
        <td>ID</td>
    </tr>
    <tr align='center'>
        <td>customers</td>
        <td>0</td>
        <td>UNIQUE_ID</td>
        <td>1</td>
        <td>NAME</td>
    </tr>
</table>

### <span style='color: #A0522D'><strong>Updating with Duplicate Values</strong></span>

<p>If we try to update the columns that have unique index with duplicate values, the database engine generates an error.</p>

<p><strong>Example</strong></p>

<p>Assume the previously created CUSTOMERS table and create a unique index on the column named <strong>ADDRESS</strong> using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE UNIQUE INDEX</span> <span style='color: #000000'>ADD_UNIQUE_INDEX</span> 
        <span style='color: #BD6B09'>ON</span> <span style='color: #000000'>CUSTOMERS</span>(<span style='color: #000000'>ADDRESS</span>);
      </strong>
    </td>
  </tr>
</table>

<p>Now, let us update the value in the column named ADDRESS with a duplicate (already existing data) value using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>UPDATE</span> <span style='color: #000000'>CUSTOMERS</span> 
        <br><span style='color: #BD6B09'>SET</span> <span style='color: #000000'>ADDRESS = 'Mumbai'</span> 
        <br><span style='color: #BD6B09'>WHERE</span> <span style='color: #000000'>ADDRESS = 'Delhi'</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>Output</strong></p>

<p>On executing the above query, the output is displayed as follows:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      ERROR 1062 (23000): Duplicate entry 'Mumbai' for key 'customers.ADD_UNIQUE_INDEX'
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>Creating a unique index on Multiple Fields</strong></span>

<p>We can also create a unique index on multiple fields or columns of a table using the CREATE UNIQUE INDEX statement. To do so, you just need to pass the name of the columns (you need to create the index on) to the query.</p>

<p><strong>Example</strong></p>

<p>Instead of creating a new table, let us consider the previously created CUSTOMERS table. We will create a unique index on the columns NAME and AGE using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE UNIQUE INDEX</span> <span style='color: #000000'>MUL_UNIQUE_INDEX</span> 
        <br><span style='color: #BD6B09'>ON</span> <span style='color: #000000'>CUSTOMERS</span> 
        <br><span style='color: #BD6B09'>(<span style='color: #000000'>NAME</span>, <span style='color: #000000'>AGE</span>)</span>;
      </strong>
    </td>
  </tr>
</table>

<p><strong>Output</strong></p>

<p>When we execute the above query, the output is obtained as follows:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <span>Query OK, 0 rows affected (0.04 sec)<br>
      Records: 0  Duplicates: 0  Warnings: 0.</span>
    </td>
  </tr>
</table>

<p><strong>Verification</strong></p>

<p>Now, let us list all the indexes that are created on the CUSTOMERS table using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SHOW INDEX</span> <span style='color: #BD6B09'>FROM</span> <span style='color: #000000'>CUSTOMERS</span>;
      </strong>
    </td>
  </tr>
</table>

<p>As you observe you can find the column names NAME, and AGE along with the ID (PRIMARY KEY) in the list of indexes.</p>

<table align='center'>
    <tr align='center' style='background-color: #C8E2B1'>
        <th>Table</th>
        <th>Non_unique</th>
        <th>Key_name</th>
        <th>Seq_in_index</th>
        <th>Column_name</th>
    </tr>
    <tr align='center'>
        <td>customers</td>
        <td>0</td>
        <td>PRIMARY</td>
        <td>1</td>
        <td>ID</td>
    </tr>
    <tr align='center'>
        <td>customers</td>
        <td>0</td>
        <td>MUL_UNIQUE_INDEX</td>
        <td>1</td>
        <td>NAME</td>
    </tr>
    <tr align='center'>
        <td>customers</td>
        <td>0</td>
        <td>MUL_UNIQUE_INDEX</td>
        <td>2</td>
        <td>AGE</td>
    </tr>
</table>
