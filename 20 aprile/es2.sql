

SELECT DISTINCT Name, Population FROM world.city
WHERE Population > 1000000 AND Countrycode = 'USA'
order by Population desc
