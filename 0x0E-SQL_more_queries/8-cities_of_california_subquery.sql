-- Selects records from a table (cities) with 
-- column value  found in another set

SELECT id, name FROM cities
    WHERE state_id IN
    (
        SELECT id FROM states
            WHERE name = 'California'
    )
    ORDER BY id ASC;
