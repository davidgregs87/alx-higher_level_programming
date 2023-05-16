-- A script to print the list of record with the same score
SELECT score, count(score) as number FROM second_table GROUP BY score ORDER BY score DESC;
