# esercizio 1
select libri.titolo, libri.autore, vendite.data_vendita, vendite.negozio 
from libri
inner join vendite on libri.id = vendite.id_libro
where libri.autore like '%King%'
order by vendite.data_vendita desc;

# esercizio 2 
select libri.titolo, libri.anno_pubblicazione, libri.prezzo, vendite.data_vendita
from libri
left join vendite on libri.id = vendite.id_libro
where libri.anno_pubblicazione between 2000 and 2010;

# esercizio 3
select libri.titolo, vendite.negozio, vendite.quantita, (vendite.quantita * libri.prezzo) as prezzo_totale
from libri
inner join vendite on libri.id = vendite.id_libro
where vendite.negozio IN ("9 Oriole Lane", "98558 Milwaukee Point", "98016 Esch Trail");

# esercizio 4
select libri.titolo, vendite.data_vendita, libri.prezzo, vendite.quantita
from libri
right join vendite on libri.id = vendite.id_libro
where vendite.data_vendita between '2020-01-01' and '2022-12-31'
and vendite.negozio like '%Drive%';

# esercizio 5
select libri.titolo, libri.autore, libri.prezzo, vendite.data_vendita
from libri
inner join vendite on libri.id = vendite.id_libro
where libri.genere in ('Fantasy', 'Horror', 'Drama')
and vendite.negozio like '%Plaza%'
order by vendite.data_vendita DESC;



