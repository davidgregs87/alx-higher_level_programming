-- List all cities in california in hbtn_0d_2
SELECT cities.id,cities.name
FROM cities,states
WHERE cities.state_id = states.id AND states.name = "California";
