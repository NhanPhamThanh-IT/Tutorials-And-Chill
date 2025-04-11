-- Problem: Use the database with name is 'Example' (If it isn't existed in DBMS, you must create database 'Example').

-- Switch to the master database to ensure the correct context for database operations
USE master;
GO

-- Check if a database named 'Example' exists
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'Example')
BEGIN
    -- If the database does not exist, create a new database named 'Example'
    CREATE DATABASE Example;
END
GO

-- Switch to the newly created (or existing) 'Example' database
USE Example;
GO