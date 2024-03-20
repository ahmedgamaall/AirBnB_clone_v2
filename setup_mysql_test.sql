-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbtn_0c_0t;

CREATE USER IF NOT EXISTS 'hbtn_ts'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

USE hbtn_ts;
GRANT ALL PRIVILEGES 
ON `hbtn_0c_0t`.*
TO 'hbtn_ts'@'localhost';
GRANT SELECT 
ON `performance_schema`.*
TO 'hbtn_ts'@'localhost';