-- lists all the cities of CArlifornia
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'Carlifornia') ORDER BY id ASC;
