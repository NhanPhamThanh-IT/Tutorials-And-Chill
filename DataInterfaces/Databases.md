<div align='justify'>

# <div align='center'>Databases</div>

The data is Relational database systems are stored in a normalized format. So, to carry out statistical computing we will need very advanced and complex Sql queries. But R can connect easily to many relational databases like MySql, Oracle, Sql server etc. and fetch records from them as a data frame. Once the data is available in the R environment, it becomes a normal R data set and can be manipulated or analyzed using all the powerful packages and functions.

In this tutorial we will be using MySql as our reference database for connecting to R.

## RMySQL Package

R has a built-in package named "RMySQL" which provides native connectivity between with MySql database. You can install this package in the R environment using the following command.

```r
install.packages("RMySQL")
```

## Connecting R to MySql

Once the package is installed we create a connection object in R to connect to the database. It takes the username, password, database name and host name as input.

```r
# Create a connection Object to MySQL database.
# We will connect to the sampel database named "sakila" that comes with MySql installation.
mysqlconnection = dbConnect(MySQL(), user = 'root', password = '', dbname = 'sakila', host = 'localhost')

# List the tables available in this database.
dbListTables(mysqlconnection)
```

When we execute the above code, it produces the following result:

```
[1] "actor"                      "actor_info"                
 [3] "address"                    "category"                  
 [5] "city"                       "country"                   
 [7] "customer"                   "customer_list"             
 [9] "film"                       "film_actor"                
[11] "film_category"              "film_list"                 
[13] "film_text"                  "inventory"                 
[15] "language"                   "nicer_but_slower_film_list"
[17] "payment"                    "rental"                    
[19] "sales_by_film_category"     "sales_by_store"            
[21] "staff"                      "staff_list"                
[23] "store"
```

## Querying the Tables

We can query the database tables in MySql using the function dbSendQuery(). The query gets executed in MySql and the result set is returned using the R fetch() function. Finally it is stored as a data frame in R.

</div>