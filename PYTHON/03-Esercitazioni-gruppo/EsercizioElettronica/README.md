# Analisi

# L'eserczio ci chiede la gestione di un negozio 

# gli elementi che abbiamo da gestire sono

- prodotti
- clienti 
- negozio stesso

Il programma ci deve permettere di aggiungere prodotti, registrare clienti, vendere prodotti e gestire le 
scorte.

## Creazione Database

- Prodotti
    - id_prodotto
    - nome
    - quantità

- Clienti
    - id_cliente
    - nome
    - cognome
    - email
    - numero

## Gestione menù

All'avvio del programma ci sarà un menù con delle opzioni selezionabili
digitando un numero, dopo aver scelto l'opzione il programma non si chiuderà ma ci darà la possibilità di scegliere altre opzioni, ci sarà un'opzione per chiudere il programma

## Gestione Inserimento Prodotti

Quando si sceglie l'opzione per inserire i prodotti allora bisognerà inserire tutte le informazioni richiesto (es. nome) e alla fine verrà inserito nel database, con valore default di quantità 0

## Gestione Inserimento Clienti

Per inserire i clienti bisognerà inserire tutte le informazioni e alla fine verrà inserito nel database

## Aggiungere scorte di un prodotto

Quando si sceglie questa opzione, se non ci sono prodotti, allora stampera "Non ci sono prodotti", in caso constrario, ci uscirà una lista dei nomi dei prodotti, la loro quantità, e il loro id
