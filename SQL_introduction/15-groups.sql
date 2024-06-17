-- Script that lists the number of records with the same score int he table second_table
SELECT score, COUNT(score) number
FROM second_table
GROUP BY score
ORDER By score DESC;