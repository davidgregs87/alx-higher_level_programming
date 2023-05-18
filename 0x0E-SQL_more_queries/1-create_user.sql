-- Create a new user, set their password, grant this user all permission
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = PASSWORD('user_0d_1_pwd');
GRANT ALL PRIVILEGES ON '*' TO  'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

