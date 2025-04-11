-- Problem: We need rename database with the beginning name is 'Test' and now we want to rename it into 'Example'.

-- Set the context to the master database, which is necessary for database creation and modification
USE master;

-- Check if a database named 'Test' does not exist
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'Test')
BEGIN
    -- If the database 'Test' does not exist, create it
    CREATE DATABASE Test;
END;

-- Rename the database 'Test' to 'Example'
ALTER DATABASE Test MODIFY NAME = Example;