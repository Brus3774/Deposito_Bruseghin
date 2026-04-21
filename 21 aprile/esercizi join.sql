
SELECT 
    Clienti.nome, 
    Ordini.data_ordine, 
    Ordini.importo
FROM Clienti
INNER JOIN Ordini ON Clienti.id = Ordini.id_cliente;

-- valore ordine anomalo
INSERT INTO Clienti (id, nome, città) VALUES (99, 'Cliente Test', 'Roma');

-- disattivazione controllo e inserimento cliente anomalo
SET FOREIGN_KEY_CHECKS = 0; -- Disattiva i controlli
INSERT INTO Ordini (id, id_cliente, data_ordine, importo) 
VALUES (999, 5000, '2024-01-01', 10.00);

SET FOREIGN_KEY_CHECKS = 1; -- Riattiva i controlli

SELECT
Clienti.nome, 
Ordini.data_ordine, 
Ordini.importo
FROM Clienti
LEFT JOIN Ordini ON Clienti.id = Ordini.id_cliente;


SELECT
Clienti.nome, 
Ordini.data_ordine, 
Ordini.importo
FROM Clienti
right JOIN Ordini ON Clienti.id = Ordini.id_cliente;

