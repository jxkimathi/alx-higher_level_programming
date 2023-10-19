-- ists all the cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON stated.id = cities.states.id ORDER BY sities.id;
