-- Create a database, create a user and grant select permission on the user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT PERMISSION ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
