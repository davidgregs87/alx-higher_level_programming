-- create database, create user and grant only select privilege to user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2;
SET PASSWORD TO 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT PERMISSION ON hbtn_0d_0 TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
