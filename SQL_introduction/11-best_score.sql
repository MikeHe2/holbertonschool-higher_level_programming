-- Script that lists all records with a score >= 10 of the table second_table of a databas
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
