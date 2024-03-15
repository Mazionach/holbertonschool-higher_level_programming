-- print all cities and their state, ordered by city id

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id;
