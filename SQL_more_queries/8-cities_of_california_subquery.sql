-- list all cities of california
SELECT id, name FROM citiesWHERE state_id = (
	SELECT id FROM states WHERE name = "California"
);
