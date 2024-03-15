-- list all records from table ordered by score
-- skip records without name
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
