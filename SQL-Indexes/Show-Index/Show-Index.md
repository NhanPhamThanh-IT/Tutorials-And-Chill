<div style='text-indent: 0 cm; background-color: white; color: black; padding-top: 20px; padding-bottom: 10px;'>

# <span style='display: flex; justify-content: center; color: #E54646'><b>Show Indexes</b></span>

<div align='justify'>
<blockquote style='background-color: white; color: black'>

### <span style='color: #A0522D'><strong>The SQL Show Index Statement</strong></span>

<p>The <strong>SHOW INDEX</strong> is the basic SQL statement to retrieve the information about the indexes that have been defined on a table. However, the SHOW INDEX statement only works on MySQL RDBMS and is not a valid statement in the SQL Server.</p>

<table style='background-color: #FFE4B5'>
  <tr>
    <td style='border: solid white'>To list the indexes created on a table in SQL Server, a system stored procedure <strong>sp_helpindex</strong> is used.
    </td>
  </tr>
</table>

<p>The result-set obtained from querying the SHOW INDEX statement on a MySQL table contains the index information.</p>

### <span style='color: #A0522D'><strong>Syntax</strong></span>

<p>Following is the syntax of the <strong>SHOW INDEX</strong> statement in MySQL</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SHOW</span> <span style='color: #000000'>INDEX</span> 
        <span style='color: #BD6B09'>FROM</span> <span style='color: #000000'>table_name</span>;
      </strong>
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>Example</strong></span>

<p>Following example demonstrates the working of SHOW INDEX statement in MySQL. First, create a table with the name CUSTOMERS in the MySQL database using the CREATE query below:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE TABLE</span> <span style='color: #000000'>CUSTOMERS</span> (
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>ID</span> <span style='color: #BD6B09'>INT</span> <span style='color: #BD6B09'>NOT NULL</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>NAME</span> <span style='color: #BD6B09'>VARCHAR</span> (<span style='color: #000000'>20</span>) <span style='color: #BD6B09'>NOT NULL</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>AGE</span> <span style='color: #BD6B09'>INT</span> <span style='color: #BD6B09'>NOT NULL</span>,
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>ADDRESS</span> <span style='color: #BD6B09'>CHAR</span> (<span style='color: #000000'>25</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span>SALARY</span> <span style='color: #BD6B09'>DECIMAL</span> (<span style='color: #000000'>20</span>, <span style='color: #000000'>2</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #BD6B09'>PRIMARY KEY</span> (<span>ID</span>)
        <br>);
      </strong>
    </td>
  </tr>
</table>

<p>Let us now insert some values into the above created table using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>INSERT INTO</span> <span style='color: #000000'>CUSTOMERS</span>
        <br><span style='color: #BD6B09'>VALUES</span>
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>1</span>, <span style='color: #000000'>'Ramesh'</span>, <span style='color: #000000'>'32'</span>, <span style='color: #000000'>'Ahmedabad'</span>, <span style='color: #000000'>2000</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>2</span>, <span style='color: #000000'>'Khilan'</span>, <span style='color: #000000'>'25'</span>, <span style='color: #000000'>'Delhi'</span>, <span style='color: #000000'>1500</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>3</span>, <span style='color: #000000'>'Kaushik'</span>, <span style='color: #000000'>'23'</span>, <span style='color: #000000'>'Kota'</span>, <span style='color: #000000'>2000</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>4</span>, <span style='color: #000000'>'Chaitali'</span>, <span style='color: #000000'>'25'</span>, <span style='color: #000000'>'Mumbai'</span>, <span style='color: #000000'>6500</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>5</span>, <span style='color: #000000'>'Hardik'</span>, <span style='color: #000000'>'27'</span>, <span style='color: #000000'>'Bhopal'</span>, <span style='color: #000000'>8500</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>6</span>, <span style='color: #000000'>'Komal'</span>, <span style='color: #000000'>'22'</span>, <span style='color: #000000'>'Hyderabad'</span>, <span style='color: #000000'>9000</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #000000'>7</span>, <span style='color: #000000'>'Muffy'</span>, <span style='color: #000000'>'24'</span>, <span style='color: #000000'>'Indore'</span>, <span style='color: #000000'>5500</span>);
      </strong>
    </td>
  </tr>
</table>

<p>Once the data is inserted, create an index for the column <strong>NAME</strong> in the CUSTOMERS table using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE INDEX</span> <span style='color: #000000'>INDEX_NAME</span>
        <br><span style='color: #BD6B09'>ON</span> <span style='color: #000000'>CUSTOMERS</span>
        <br><span style='color: #BD6B09'>()</span> <span style='color: #000000'>(NAME)</span>;
      </strong>
    </td>
  </tr>
</table>

<p>Now, you can list all the indexes that are defined on the CUSTOMERS table using the following query:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>SHOW INDEX</span> 
        <br><span style='color: #BD6B09'>FROM</span> <span style='color: #000000'>CUSTOMERS</span>;
      </strong>
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>Output</strong></span>

<p>On executing the above query, the output is displayed as follows:</p>

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
        <td>1</td>
        <td>index_name</td>
        <td>1</td>
        <td>NAME</td>
    </tr>
</table>

### <span style='color: #A0522D'><strong>Showing Indexes in SQL Server</strong></span>

<p>In SQL server, the system stored procedure <strong>sp_helpindex</strong> is used to retrieve the information about the indexes that have been defined on a table. It returns the result as a table that contains detailed information about each index, including the name, type, and columns.</p>

### <span style='color: #A0522D'><strong>Syntax</strong></span>

<p>Following is the basic syntax to list indexes defined on a table in SQL Server:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>sp_helpindex</span> 
        <br><span style='color: #BD6B09'>[</span> <span style='color: #000000'>@objname =</span> <span style='color: #BD6B09'>'name'</span> <span style='color: #BD6B09'>]</span>;
      </strong>
    </td>
</tr>
</table>

<p>Here, <strong>[ @objname = ] 'name'</strong> specifies the name of the table for which the index information is being retrieved. The index information includes:</p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>index_name</strong> − The names of the columns that are included in the index.</li>
      <li><strong>index_description</strong> − A brief description of the index, such as the type of index (like clustered or non-clustered).</li>
      <li><strong>index_keys</strong> − The keys that are included in the index.</li>
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>Example</strong></span>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>CREATE INDEX</span> <span style='color: #000000'>INDEX_NAME</span>
        <br><span style='color: #BD6B09'>ON</span> <span style='color: #000000'>CUSTOMERS</span>(<span style='color: #000000'>NAME</span>);
      </strong>
    </td>
  </tr>
</table>

<p>Now, let us list all the indexes that are created on the CUSTOMERS table using the system stored procedure <strong>sp_helpindex</strong> as shown below:</p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #BD6B09'>EXEC</span> <span style='color: #000000'>sys.sp_helpindex</span> <span style='color: #BD6B09'>@objname =</span> <span style='color: #000000'>N'CUSTOMERS'</span>;
      </strong>
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>Output</strong></span>

<p>On executing the above query, the output is displayed as follows:</p>

<table align='center'>
    <tr align='center' style='background-color: #F0F0F0'>
        <th>index_name</th>
        <th>index_description</th>
        <th>index_keys</th>
    </tr>
    <tr align='center'>
        <td>INDEX_NAME</td>
        <td>nonclustered located on PRIMARY</td>
        <td>NAME</td>
    </tr>
    <tr align='center'>
        <td>PK__CUSTOMER__3214EC27755869D9</td>
        <td>clustered, unique, primary key located on PRIMARY</td>
        <td>ID</td>
    </tr>
</table>
