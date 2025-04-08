create table biblioteche(
nome varchar(100) not null,
indirizzo varchar (100) not null,
city varchar(100) not null,
phone_number varchar (10),
giorno_settimana varchar(50),
orario_apertura time,
orario_chiusura time,
id_biblioteca int not null auto_increment primary key
);

create table libri(
ISBN varchar(13) primary key,
titolo varchar(100) not null,
autore varchar(100) not null,
genere varchar(50),
anno_pub varchar(50),
id_copia int not null,
stato varchar (50)
);

create table utenti(
id_utente int not null auto_increment primary key,
nome varchar(100) not null,
cognome varchar(100) not null,
born_date varchar(50),
phone_number varchar (10)
);

create table iscrizioni(
id_iscrizione int not null auto_increment primary key,
id_utente int not null references utenti(id_utente),
id_biblioteca int not null references biblioteche(id_biblioteca)
);

create table prestiti(
id_prestito int not null auto_increment primary key,
id_utente int not null references utenti(id_utente),
ISBN varchar(13) references libri(ISBN),
id_biblioteca int not null references biblioteche(id_biblioteca),
ottenuto date,
scadenza date,
restituzione date
);

create table prenotazioni(
id_prenotazione int not null auto_increment primary key,
id_utente int not null references utenti(id_utente),
id_biblioteca int not null references biblioteche(id_biblioteca),
ISBN varchar(13) not null,
prenotazione date
);

create table eventi(
id_evento int not null auto_increment primary key,
titolo varchar(100) not null,
descrizione varchar(200),
giorno date,
orario time,
id_biblioteca int not null references biblioteche(id_biblioteca),
max_ppl int
);

create table partecipazioni(
id_presenza int not null auto_increment primary key,
id_utente int not null references utenti(id_utente),
id_evento int not null references eventi(id_evento)
);

insert into biblioteche (nome, indirizzo, city) value
('Biblioteca Centrale', 'Via Diomede 1', 'Milano'),
('Biblioteca Nord', 'Via Garibaldi 32', 'Torino'),
('Biblioteca Sud', 'Via Falconi 3', 'Napoli'),
('Biblioteca Est', 'Via Manzoni 27', 'Firenze'),
('Biblioteca Ovest', 'Via Dante 5', 'Bologna');

insert into utenti (nome, cognome, born_date, phone_number) values
('Alexander', 'Caves', '2004-05-08', '3338621234'),
('Simone', 'Pizzorno', '2005-01-26', '3922767770'),
('Domenico', 'Vardè', '2004-06-21', '3457191009'),
('Tommaso', 'Ferrero', '2003-06-06', '3288484821'),
('Andrea', 'Sabini', '1999-02-28', '3933666886'),
('Alessandro', 'Defilippis', '2002-06-04', '3402366458');

insert into iscrizioni (id_utente, id_biblioteca) values
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

insert into libri (ISBN, titolo, autore, genere, anno_pub, id_copia, stato) values
('9781234567897', 'Eppure Cadiamo Felici', 'Enrico Galiano', 'Romanzo', 2017, 3, 'Ottimo'),
('9789876543210', '1984', 'George Orwell', 'Distopia', 1949, 2, 'Buono'),
('9781111111111', 'Don Chisciotte', 'Miguel de Cervantes', 'Storico', 1605, 1, 'Ottimo'),
('9782222222222', 'Sherlock Holmes: Uno Studio in Rosso', 'Arthur Conan Doyle', 'Giallo', 1887, 2, 'Ottimo'),
('9783333333333', 'Orgoglio E Pregiudizio', 'Jane Austen', 'Romantico', 1813, 4, 'Danneggiato');

insert into prestiti (id_utente, ISBN, id_biblioteca, ottenuto, scadenza, restituzione) values
(1, '9782222222222', 2, '2025-02-20', '2025-02-20', '2025-02-18'),
(2, '9781234567897', 4, '2025-02-21', '2025-03-21', null),
(2, '9782222222222', 4, '2025-02-21', '2025-03-21', null),
(4, '9783333333333', 5, '2025-02-19', '2025-02-19', '2025-02-14'),
(3, '9781111111111', 3, '2025-02-21', '2025-03-21', null);

insert into prenotazioni (id_utente, id_biblioteca, ISBN, prenotazione)values
(3, 4, '9782222222222', '2025-03-24'),
(1, 3, '9781111111111', '2025-03-24'),
(5, 3, '9781111111111', '2025-04-24');

insert into eventi (titolo, descrizione, giorno, orario, id_biblioteca, max_ppl)values
('Incontro Con L Autore', 'Presentazione Libro', '2025-03-01', '18:00', 1, 50),
('Workshop Di Scrittura', 'Laboratorio Per Aspiranti Scrittori', '2025-03-10', '16:00', 2, 30),
('Lettura Condivisa', 'Discussione Di Un Classico', '2025-03-15', '17:00', 3, 40),
('Serata Poesia', 'Lettura Di Poesie Con Autori Ospiti', '2025-03-20', '19:00', 1, 35),
('Conferenza Storica', 'Approfondimento Su Eventi Del Passato', '2025-03-25', '17:30', 2, 40);

insert into partecipazioni (id_utente, id_evento)values
(1, 1),
(2, 2);

-- Elencare tutti i libri disponibili in una specifica biblioteca.
select *
from libri
join biblioteche ;
-- Trovare gli utenti con più di 3 libri in prestito attualmente.
select nome, cognome
from utenti;
-- Elencare i prestiti attivi di un determinato utente.

-- Elencare tutti gli eventi in una specifica biblioteca ordinati per data.
select titolo, descrizione, giorno, orario, id_biblioteca
from eventi
where id_biblioteca = 2
order by giorno;
-- Verificare quali libri hanno il maggior numero di prenotazioni.

-- Trovare i libri più frequentemente prestati nell’ultimo anno.

-- Elencare le biblioteche con il maggior numero di prestiti attivi.

-- Visualizzare gli utenti iscritti a più di una biblioteca.

-- Trovare i libri danneggiati presenti in una biblioteca specifica.
select titolo, autore, stato
from libri 
where stato = 'Danneggiato';
-- Trovare gli eventi con più iscritti e verificare se hanno ancora posti disponibili.




