-- Risolvere le seguenti query

-- Selezione le ripartizioni geografiche d'Italia

SELECT * FROM RipartizioneGeografica

-- Selezionare tutte le regioni d'Italia

SELECT * from Regione

-- Selezionare le provincie d'Italia in ordine alfabetico crescente

select * from Provincia order by Denominazione asc

-- Selezionare le regione del Nord-Ovest

select Regione.Denominazione as 'Regione'
from regione 
INNER JOIN  RipartizioneGeografica ON Regione.IdRipartizione = RipartizioneGeografica.id
WHERE RipartizioneGeografica.Denominazione = 'Nord-Ovest'

-- Visualizzare la provincia e la sigla automobilistica delle provincie della regione Toscana



-- Visualizzare il comune, il codice catastale, la provincia di tutti i comuni appartenenti al Piemonte



-- Visualizzare la regione, la provincia, il comune che hanno altitudine dal centro minore di 500 metri



-- Visualizzare la popolazione al 2011 della provincia di Torino



-- Quanti sono i comuni del Nord-Est



-- Quale comune ha il maggior numero di abitanti nel 2001



-- Visualizzare la popolazione nel 2011 minore d'Italia



-- Visualizzare la superficie media dei comuni della provincia di Salerno



-- Visualizzare la ripartizione geografica, la regione, la provincia, il comune, la zona litoranea, l'altitudine dal centro, la superficie, la zona montana, la zona altimetrica di tutti i comuni capoluoghi


