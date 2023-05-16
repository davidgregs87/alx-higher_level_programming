-- first we need to download the file to our terminal/machine
-- use the command to download it: curl -O[URL] it will download temperatures.sql and save it on your machine
-- import that file to your database with: mysql "username" -p "DB_name" < "SQL_file"
-- Let's now retrieve our informations
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
