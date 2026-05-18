-- esercizio 1
SELECT 
    c.Name AS Citta,
    co.Name AS Nazione,
    cl.Language AS 'Lingua Ufficiale'
FROM 
    city AS c
INNER JOIN 
    country AS co ON c.CountryCode = co.Code
INNER JOIN 
    countrylanguage AS cl ON co.Code = cl.CountryCode
WHERE 
    cl.IsOfficial = 'T'; -- 'T' sta per True (Vero) -- significa che il database prende l'elenco di tutte le città e le loro lingue, controlla la colonna IsOfficial e scarta tutte le righe in cui non c'è scritto 'T'

-- esercizio 2

SELECT 
    co.Name AS Nazione,
    COUNT(c.ID) AS Numero_Citta
FROM 
    city AS c
INNER JOIN 
    country AS co ON c.CountryCode = co.Code
GROUP BY 
    co.Name
ORDER BY 
    Numero_Citta DESC; -- DESC serve per mettere le nazioni con più città in alto
    
-- esercizio 3
SELECT 
    co.Name AS Nazione,
    co.LifeExpectancy AS Aspettativa_Vita,
    co.GovernmentForm AS Forma_Governo,
    cl.Language AS Lingua
FROM 
    country AS co
INNER JOIN 
    countrylanguage AS cl ON co.Code = cl.CountryCode
WHERE 
    co.GovernmentForm LIKE '%Republic%' 
    AND co.LifeExpectancy > 70; 

-- esercizio 4 

SELECT 
    co.Name AS Nazione,
    cl.Language AS Lingua,
    cl.Percentage AS Percentuale_Utilizzo
FROM 
    country AS co
INNER JOIN 
    countrylanguage AS cl ON co.Code = cl.CountryCode
ORDER BY 
    co.Name ASC, 
    cl.Percentage DESC;
    
-- esercizio 5

SELECT 
    co.Name AS Nazione,
    MAX(cl.Percentage) AS Percentuale_Massima
FROM 
    country AS co
INNER JOIN 
    countrylanguage AS cl ON co.Code = cl.CountryCode
GROUP BY 
    co.Name
ORDER BY 
    co.Name;

-- esercizio 6

SELECT 
    co.Name AS Nazione,
    cl.Language AS Lingua_Piu_Parlata,
    max_lingue.Percentuale_Massima AS Percentuale
FROM 
    country AS co
INNER JOIN 
    countrylanguage AS cl ON co.Code = cl.CountryCode
INNER JOIN (
    -- Subquery
    SELECT 
        CountryCode, 
        MAX(Percentage) AS Percentuale_Massima
    FROM 
        countrylanguage
    GROUP BY 
        CountryCode
) AS max_lingue ON cl.CountryCode = max_lingue.CountryCode 
               AND cl.Percentage = max_lingue.Percentuale_Massima
ORDER BY 
    co.Name;