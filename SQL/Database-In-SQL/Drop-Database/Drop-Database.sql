-- Problem: Let's say we have created a database named QLY_HOCSINH previously (or already exists in the DBMS).
-- How can we drop the database QLY_HOCSINH out of DBMS.

-- Switch to the master database to ensure you are not using the database to be dropped
USE master;

-- Check if the database exists before attempting to drop it
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'QLY_HOCSINH')
BEGIN
    -- Drop the database
    DROP DATABASE QLY_HOCSINH;
    PRINT 'Database QLY_HOCSINH dropped successfully';
END
ELSE
BEGIN
    PRINT 'Database QLY_HOCSINH does not exist';
END