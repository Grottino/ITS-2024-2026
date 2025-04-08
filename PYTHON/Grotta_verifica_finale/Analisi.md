# SISTEMA DI GESTIONE DI PRENOTAZIONE PER VISITE MEDICHE
### Obbiettivo principale
Creazione di un programma che gestisca un sistema di prenotazione per visite mediche facendo in modo di registrare i dati immessi dall'utente nel database senza spaccarsi

### Obbiettivo secondario
Rendere lo script meno sporco e più efficente possibile evitando ripetizioni e facendo in modo che gli output siano distinti e leggibili

## 0. Struttura del Sistema

Il compito deve essere suddiviso in queste sorgenti:

Medico.py = Classe per contenere l'oggetto medico e mapparlo

Paziente.py = Classe per contenere l'oggetto Paziente e mapparlo

Visita.py = Classe per contenere l'oggetto Visita e mapparlo

dump.py = Script per la creazione delle tabelle nel database

DatabaseUtilities.py = Classe per la gestione del database


Controlli.py = File per evitare che si possano mettere determinati caratteri negli input (ControlloVuoto, ControlloNoNumeri, ControlloInizioNumeri, ControlloNoLettere)

main.py = File di scrittura principale che verrà utilizzato dall'utente 

## 1. Creazione del Database (30 min)
Importare sqlite3    

Fare la connessione al db e inserire il cursore

Droppare le tabelle in caso esistano già (DELETE IF EXIST, CREATE TABLE IF NOT EXIST)

Scrivere il database immettendo le varie classi citate nel file di testo(guarda il punto 0)(cur.execute('''))

Inserire le informazione che riguardano le classi individualmente:
- Pazienti (id_paziente come chiave primaria, nome, cognome, anno_nascita)
- Medici (id_medico primary key,nome, cognome)
- Visite(numeroVisita primary key, nomePaziente, nomeMedico, giorno, mese)

## 2. Creazione delle classi (15 min)

Creare le classi basandosi sul database (mettendole al singolare)

Inizializzarle con l'utilizzo del self

## 3. Gestione del Database (20 min)

Connettere il database

Fare in modo di immagazzinare i dati chiesti in input 

## 4. Sviluppo del Main (1 ora)

Importare tutto

Scrivere le scelte che l'utente potrà effettuare:  
0. Esci dal programma
1. Registrare pazienti
2. Registrare medici
3. Organizzare visite

Sviluppare le scelte con gli if

Printare una frase in caso di successo

## 5. Gestione degli Errori (20 min)

Utilizzare il costrutto try-except per evitare che si spacchi

Creare i controlli nella sorgente apposita ed applicarli nei vari input

## 6. Test e Debug (quando mancano 30 min)

- Testare che il programma funzioni

- Verificare che i controlli facciano il loro lavoro

- Controllare se i dati sono stati effettivamente messi nel database

- Pulire e ordinare il README

- Rendere il codice più efficente

- Commentare il codice