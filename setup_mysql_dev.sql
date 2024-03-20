-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

CREATE USER IF NOT EXISTS 'hbtn_d'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

USE hbtn_0c_0;
GRANT ALL PRIVILEGES 
ON `hbtn_0c_0`.*
TO 'hbtn_d'@'localhost';
GRANT SELECT 
ON `performance_schema`.*
TO 'hbtn_d'@'localhost';