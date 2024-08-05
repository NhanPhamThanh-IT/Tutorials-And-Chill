-- Switch to the master database
USE master;

-- Check if the database QLY_HOCSINH exists
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'QLY_HOCSINH')
BEGIN
    -- If it exists, print a message
    PRINT 'Database exists';
END
ELSE
BEGIN
    -- If it does not exist, print a different message
    PRINT 'Database does not exist';
END

-- Create the database QLY_HOCSINH
CREATE DATABASE QLY_HOCSINH;

-- Switch to the newly created database
USE QLY_HOCSINH;