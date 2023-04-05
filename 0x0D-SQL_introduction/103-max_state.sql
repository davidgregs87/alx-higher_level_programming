-- script that displays the max temperature of each state (ordered by State name).
-- Importing:  mysql -u username -p  databasename  < path/example.sql
SELECT `state`, MAX(`value`) AS max_temp
FROM temperatures
GROUP BY `state`
ORDER BY `state` ASC;
