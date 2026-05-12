-- SELEZIONE DEL DATABASE
USE vendite;

-- 1. Numero totale di vendite per categoria
SELECT categoria, COUNT(*) AS numero_vendite
FROM Vendite
GROUP BY categoria;

-- 2. Prezzo medio per categoria
SELECT categoria, AVG(prezzo_unitario) AS prezzo_medio
FROM Vendite
GROUP BY categoria;

/* 
   3. Totale quantità vendute per prodotto
   Questa query somma tutte le unità vendute raggruppandole 
*/
SELECT prodotto, SUM(quantita) AS quantita_totale
FROM Vendite
GROUP BY prodotto
ORDER BY quantita_totale DESC;


-- 4. Prezzo massimo e minimo tra i prodotti
SELECT MAX(prezzo_unitario) AS prezzo_max, MIN(prezzo_unitario) AS prezzo_min
FROM Vendite;

-- Query 5: Conteggio totale delle vendite registrate nella tabella
SELECT COUNT(*) AS totale_vendite_registrate
FROM Vendite;

-- Query 6: I 5 prodotti più costosi (in base al prezzo unitario)
SELECT prodotto, prezzo_unitario
FROM Vendite
ORDER BY prezzo_unitario DESC
LIMIT 5;

-- Query 7: I 3 prodotti con la quantità totale più bassa venduta
SELECT prodotto, SUM(quantita) AS totale_pezzi
FROM Vendite
GROUP BY prodotto
ORDER BY totale_pezzi ASC
LIMIT 3; 