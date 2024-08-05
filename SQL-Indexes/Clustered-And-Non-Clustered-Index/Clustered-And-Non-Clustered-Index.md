<div style='text-indent: 0 cm; background-color: white; color: black; padding-top: 20px; padding-bottom: 10px;'>

# <span style='display: flex; justify-content: center; color: #E54646'><b>Difference Between Clustered and Non-Clustered Index</b></span>

<div align='justify'>
<blockquote style='background-color: white; color: black'>

<p>In SQL Server, indexing plays a crucial role in enhancing data retrieval efficiency. Indexes are disk-based structures linked to tables or views, aiding in quicker row retrieval by organizing data in a structured manner. Two primary types of indexes in SQL Server are Clustered and Non-Clustered Indexes.</p>

<p>An index is a disk-based structure linked to a table or view that facilitates quicker row retrieval. A table or view’s table or view’s columns are used to create keys in an index. These keys are kept in a structure (B-tree) that enables SQL Server to quickly and effectively locate the row or rows that correspond to the key values.</p>

## <span><b>Clustered Index</b></span>

<p>A clustered index is created only when both the following conditions are satisfied:</p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>The data or file that you are moving into secondary memory should be in sequential or sorted order</strong> − This ensures efficient storage and retrieval.</li>
      <li><strong>There should be a key value</strong> − The key value must be unique and cannot have repeated values to maintain data integrity and facilitate effective indexing.</li>
    </td>
  </tr>
</table>

<p>Whenever you apply clustered indexing in a table, it will perform sorting in that table only. You can create only one clustered index in a table like a primary key. A clustered index is as same as a dictionary where the data is arranged in alphabetical order.</p>

<p>In a clustered index, the index contains a pointer to block but not direct data.</p>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20200410115906/Clustered_Index.jpg' style='border: solid black 5px'><br><small><i>Example of Clustered Index</i></small></div>

### <span style='color: #A0522D'><strong>Example of Clustered Index</strong></span>

<p>If you apply the primary key to any column, then automatically it will become a clustered index.</p>

<p><strong>Create Table</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
        <span style='color: #000000'>-- Create the Student table</span>
        <br><span style='color: #BD6B09'>CREATE TABLE</span> <span style='color: #000000'>Student</span> (
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>Roll_No</span> <span style='color: #BD6B09'>INT</span> <span style='color: #BD6B09'>PRIMARY KEY</span>, 
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>Name</span> <span style='color: #BD6B09'>VARCHAR</span>(<span style='color: #008000'>50</span>), 
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>Gender</span> <span style='color: #BD6B09'>VARCHAR</span>(<span style='color: #008000'>30</span>), 
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>Mob_No</span> <span style='color: #BD6B09'>BIGINT</span>
        <br>);
        <br><span style='color: #000000'>-- Insert data into the Student table</span>
        <br><span style='color: #BD6B09'>INSERT INTO</span> <span style='color: #000000'>Student</span> 
        <br><span style='color: #BD6B09'>VALUES</span>
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #008000'>4</span>, <span style='color: #000000'>'ankita'</span>, <span style='color: #000000'>'female'</span>, <span style='color: #008000'>9876543210</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #008000'>3</span>, <span style='color: #000000'>'anita'</span>, <span style='color: #000000'>'female'</span>, <span style='color: #008000'>9675432890</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #008000'>5</span>, <span style='color: #000000'>'mahima'</span>, <span style='color: #000000'>'female'</span>, <span style='color: #008000'>8976453201</span>);
    </td>
  </tr>
</table>

<p>In this example, Roll no is a primary key, it will automatically act as a clustered index. The output of this code will produce in increasing order of roll no.</p>

<p><strong>Output</strong></p>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20230508204048/Screenshot_100.png' style='border: solid black 5px'><br><small><i>Student table</i></small></div>

<p>You can have only one clustered index in one table, but you can have one clustered index on multiple columns, and that type of index is called a composite index.</p>

<p>Here, the Roll_No column serves as the primary key, automatically becoming the clustered index. The output of querying this table will present data in ascending order of Roll_No.</p>

<p><strong>Key Differences</strong></p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>Only one clustered index is allowed per table</strong> − A table can have only one clustered index, as it defines the physical order of the data rows.</li>
      <li><strong>The clustered index directly affects the physical ordering of data</strong> − It determines the sequence in which data is stored on disk, affecting data retrieval performance.</li>
      <li><strong>It offers faster retrieval but may slow down insert and update operations</strong> − While clustered indexes speed up data retrieval, they can impact the performance of data modification operations due to the need to maintain the physical order.</li>
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>Non-Clustered Index</strong></span>

<p>The non-Clustered Index is similar to the index of a book. The index of a book consists of a chapter name and page number, if you want to read any topic or chapter then you can directly go to that page by using the index of that book. No need to go through each and every page of a book.</p>

<p>The data is stored in one place, and the index is stored in another place. Since the data and non-clustered index is stored separately, then you can have multiple non-clustered indexes in a table.</p>

<p>In a non-clustered index, the index contains the pointer to data.</p>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20200410120011/Non-clustered_Index.jpg' style='border: solid black 5px'><br><small><i>Example of Non Clustered Index</i></small></div>

### <span style='color: #A0522D'><strong>Example of Non-Clustered Index </strong></span>

<p>The given code creates a table “Student” with columns “Roll_No”, “Name”, “Gender”, and “Mob_No”. The primary key is defined on the “Roll_No” column. Three rows are inserted into the “Student” table with different values for the columns. Finally, a nonclustered index “NIX_FTE_Name” is created on the “Name” column in ascending order.</p>

<p>The “CREATE TABLE” statement is used to create a new table “Student” with four columns “Roll_No”, “Name”, “Gender”, and “Mob_No”. The “Roll_No” column is defined as the primary key of the table.</p>

<p>The “INSERT INTO” statements are used to insert three rows of data into the “Student” table. Each row contains values for all the columns of the table. The first row has a roll number of 4, the name of “Afzal”, the gender of “male”, and a mobile number of 9876543210. The second row has a roll number of 3, the name of “Sudhir”, the gender of “male”, and a mobile number of 9675432890. The third row has a roll number of 5, name of “zoya”, the gender of “female”, and a mobile number of 8976453201.</p>

<p><strong>Query</strong></p>

<table align='center' style='border: solid white; padding-top: 20px; padding-bottom: 0px;'>
  <tr>
    <td style='background-color: #F0F0F0'>
      <strong>
        <span style='color: #000000'>-- Create the Student table</span>
        <br><span style='color: #BD6B09'>CREATE TABLE</span> <span style='color: #000000'>Student</span> (
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>Roll_No</span> <span style='color: #BD6B09'>INT</span> <span style='color: #BD6B09'>PRIMARY KEY</span>, 
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>Name</span> <span style='color: #BD6B09'>VARCHAR</span>(<span style='color: #008000'>50</span>), 
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>Gender</span> <span style='color: #BD6B09'>VARCHAR</span>(<span style='color: #008000'>30</span>), 
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: #000000'>Mob_No</span> <span style='color: #BD6B09'>BIGINT</span>
        <br>);
        <br><span style='color: #000000'>-- Insert data into the Student table</span>
        <br><span style='color: #BD6B09'>INSERT INTO</span> <span style='color: #000000'>Student</span> 
        <br><span style='color: #BD6B09'>VALUES</span>
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #008000'>4</span>, <span style='color: #000000'>'afzal'</span>, <span style='color: #000000'>'male'</span>, <span style='color: #008000'>9876543210</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #008000'>3</span>, <span style='color: #000000'>'sudhir'</span>, <span style='color: #000000'>'male'</span>, <span style='color: #008000'>9675432890</span>),
        <br>&nbsp;&nbsp;&nbsp;&nbsp;(<span style='color: #008000'>5</span>, <span style='color: #000000'>'zoya'</span>, <span style='color: #000000'>'female'</span>, <span style='color: #008000'>8976453201</span>);
        <br><span style='color: #000000'>-- Create a non-clustered index on Name</span>
        <br><span style='color: #BD6B09'>CREATE NONCLUSTERED INDEX</span> <span style='color: #000000'>NIX_FTE_Name</span>
        <br><span style='color: #BD6B09'>ON</span> <span style='color: #000000'>Student</span> 
        <br><span style='color: #BD6B09'>()</span> <span style='color: #000000'>(<span style='color: #000000'>Name</span> <span style='color: #BD6B09'>ASC</span>);
      </strong>
    </td>
  </tr>
</table>

<p>Here, roll no is a primary key, hence there is automatically a clustered index. If we want to apply a non-clustered index in the NAME column (in ascending order), then a new table will be created for that column.</p>

<p><strong>Output</strong></p>

<div align='center'><img src='https://media.geeksforgeeks.org/wp-content/uploads/20230508210244/Screenshot_101.png' style='border: solid black 5px'><br><small><i>Student table</i></small></div>

<p>The row address is used because, if someone wants to search the data for Sudhir, then by using the row address he/she will directly go to that row address and can fetch the data directly.</p>

<p>In this example, the Name column is indexed in ascending order, allowing for efficient retrieval based on names.</p>

<p><strong>Key Differences</strong></p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>Multiple non-clustered indexes are allowed per table</strong> − A table can have multiple non-clustered indexes, each providing a different way to access the data.</li>
      <li><strong>Non-clustered indexes store data pointers, not the data itself</strong> − These indexes contain references to the data rows rather than the actual data, allowing quick lookups without affecting the physical storage of the data.</li>
      <li><strong>They offer flexibility but may result in slower retrieval compared to clustered indexes</strong> − While non-clustered indexes provide additional access paths, they can be less efficient for retrieval compared to clustered indexes, as they require an additional lookup to retrieve the actual data.</li>
    </td>
  </tr>
</table>

### <span style='color: #A0522D'><strong>Difference Between Clustered and Non-Clustered Index</strong></span>

<table align='center'>
    <tr align='center' style='background-color: #F0F0F0'>
        <th>CLUSTERED INDEX</th>
        <th>NON-CLUSTERED INDEX</th>
    </tr>
    <tr>
        <td>A clustered index is faster.</td>
        <td>A non-clustered index is slower.</td>
    </tr>
    <tr>
        <td>The clustered index requires less memory for operations.</td>
        <td>A non-clustered index requires more memory for operations.</td>
    </tr>
    <tr>
        <td>In a clustered index, the clustered index is the main data.</td>
        <td>In a non-clustered index, the index is a copy of data.</td>
    </tr>
    <tr>
        <td>A table can have only one clustered index.</td>
        <td>A table can have multiple non-clustered indexes.</td>
    </tr>
    <tr>
        <td>The clustered index has the inherent ability to store data on the disk.</td>
        <td>A non-clustered index does not have the inherent ability to store data on the disk.</td>
    </tr>
    <tr>
        <td>Clustered index stores pointers to blocks, not data.</td>
        <td>The non-clustered index stores both the value and a pointer to the actual row that holds the data.</td>
    </tr>
    <tr>
        <td>In a clustered index, leaf nodes are actual data itself.</td>
        <td>In a non-clustered index, leaf nodes are not the actual data itself; they only contain included columns.</td>
    </tr>
    <tr>
        <td>In a clustered index, the clustered key defines the order of data within a table.</td>
        <td>In a non-clustered index, the index key defines the order of data within the index.</td>
    </tr>
    <tr>
        <td>A clustered index is a type of index in which table records are physically reordered to match the index.</td>
        <td>A non-clustered index is a special type of index in which the logical order of the index does not match the physical stored order of the rows on the disk.</td>
    </tr>
    <tr>
        <td>The size of the primary clustered index is large.</td>
        <td>The size of the non-clustered index is comparatively smaller.</td>
    </tr>
    <tr>
        <td>Primary keys of the table by default are clustered indexes.</td>
        <td>The composite key, when used with unique constraints of the table, acts as a non-clustered index.</td>
    </tr>
</table>

### <span style='color: #A0522D'><strong>Conclusion</strong></span>

<p>In Conclusion, the decision between clustered and non-clustered indexes primarily depends on the particular requirements of your database.Choosing between clustered and non-clustered indexes depends on the specific requirements of your database:</p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>Clustered indexes are ideal for range queries and static data</strong> − They are well-suited for queries that involve ranges of values and are efficient for static datasets where the data is not frequently modified.</li>
      <li><strong>Non-clustered indexes are suitable for optimizing various query types and dynamic data environments</strong> − They provide flexibility for a wide range of query types and are effective in environments where data is frequently updated or where multiple access paths are needed.</li>
    </td>
  </tr>
</table>

<p>Understanding these indexing techniques empowers database administrators to optimize data retrieval and performance effectively.</p>

<p><strong>Index Clustering</strong></p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>Perfect for tables where range queries, in particular, place a high value on data retrieval efficiency</strong> − Clustered indexes are especially effective in scenarios where queries require efficient access to ranges of data.</li>
      <li><strong>Ideal for tables with few updates or relatively static data</strong> − Clustered indexes work best with data that does not change frequently, as the physical reordering of data can slow down insert and update operations.</li>
    </td>
  </tr>
</table>

<p><strong>Non-Clustered index</strong></p>

<table style='background-color: #FCD9C4'>
  <tr>
    <td style='border: solid white'>
      <li><strong>Allows for the optimization of various query types without changing the data’s physical order on disk</strong> − Non-clustered indexes enhance query performance by creating separate structures for data retrieval, without altering the actual data storage layout.</li>
      <li><strong>Ideal for tables where data changes often</strong> − Non-clustered indexes are well-suited for tables with frequent inserts and updates, as they generally involve less overhead compared to clustered indexes for maintaining data order.</li>
    </td>
  </tr>
</table>