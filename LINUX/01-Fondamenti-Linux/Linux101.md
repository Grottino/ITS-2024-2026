# Linux 101
## Passi Operativi
### 1. Identificazione della distribuzione e del sistema
- Il comando "cat /etc/os-release" viene usato per identificare la distribuzione e la versione (in questo caso la versione è la 24.04.2):
![alt text]({BF8FAA47-AFBC-4515-B59E-31221147D4D9}.png)

- Con "uname -r" verifichiamo la versione del kernel:
![alt text]({E211F23F-532D-4CA3-B894-21B418779A41}.png)

- Con "uname -a" mostriamo le informazioni generali del sistema:
![alt text]({B77EFB3A-A0A2-4E3A-AC92-2F8228A103F6}.png)

### 2. Navigazione nel file system e gestione di file e directory

- Grazie al comand "cd" ci muoviamo nella home directory:
![alt text]({22B7BAA5-627B-48C5-9C05-C4A310191CAD}.png)

- Usando il comando "ls -la" verranno mostrati tutti i file nella home, compresi quelli nascosti:
![alt text]({B58255CC-830E-4B45-BC02-61E0D73AF3B8}.png)

- Il comando "mkdir -p progetto/esercizi/script" creerà una directory. Per fare ciò bisogna entrare nel root:
![alt text]({A9460FD4-E4C9-4BD6-BE39-EFE1299090FE}.png)
e poi successivamente eseguire il comando:
![alt text]({443F4312-1F51-4D53-B0DF-075E69018D87}.png)

- Grazie al comando precedentemente usato ("cd") entriamo nella bellissima cartella creata:
![alt text]({F7BD5DA8-73EF-4BC0-869F-0F8551B95707}.png)

- Con "touch nome.txt" creiamo un file di testo vuoto:
![alt text]({9D669C3E-7603-4788-BCAD-77E7C2EBFE4C}.png)

- Utilizzando "ls -l" verifichiamo se è stato effettivamente creato:
![alt text]({298FA3C5-2B04-486D-813C-7907ADC8467B}.png)

- "cp file.txt directory/" ci permette di copiare il file nella cartella che menzioniamo:
![alt text]({C83A3EA1-A11E-42AD-AF4B-209A0579DF5C}.png)

- Possiamo rinominare il file usando "mv nome-attuale.txt nome-nuovo.txt":
![alt text]({1E88DF31-29A8-4AC7-A2B7-19879C27AABC}.png)

- Per eliminare il file bisogna usare "rm nome-file":
![alt text]({124E9E9A-D702-4EC2-8D23-2CB667B6A74A}.png)
### 3. Uso del terminale, pipe e redirezioni

- Usando "ls -l ~ > lista_home.txt" Eseguiamo un comando che elenchi i contenuti della home per salvarli in un file chiamato "lista_home.txt":
![alt text]({010DB9ED-5929-4B2A-A8A0-625AF9F12EE1}.png)

- Facendo "cat lista_home.txt" verifichiamo che il file "lista_home.txt" sia stato creato correttamente, guardandone il contenuto:
![alt text]({B426FDA6-74CE-44FA-ABDB-C1099EDAC5B9}.png)

- Per visualizzare tutti i processi attivi nel sistema, utilizza ps aux e accoppialo con grep per individuare una parola chiave specifica, come ad esempio "root":
![alt text]({3FA23F69-FC0F-4BC4-82DA-7D6067E17042}.png)

- Se hai a disposizione un file di testo, ad esempio lista_home.txt, puoi cercare un determinato contenuto al suo interno, come la parola "Documents":
![alt text]({89B91A02-4735-40BA-8F91-63FC92450C93}.png)

### 4. Installazione di un pacchetto open source e verifica licenza

- Aggiorna l’elenco dei pacchetti disponibili per l’installazione:
![alt text]({540AD1CE-A1EB-46A4-9A06-8B4E5AA15798}.png)

- Installa un determinato software, come tree:
![alt text]({170F4111-56A3-4A81-B296-30DF980A9603}.png)

- Controlla se il pacchetto è stato installato correttamente e verifica la versione attualmente in uso:
![alt text]({A218CB15-E831-4449-919A-FE115F37E7EE}.png)

### 5. Creazione di uno script Bash di base

- Per creare uno script accedi alla cartella script (oppure una directory di tua scelta) e crea un nuovo file chiamato mioscript.sh:
![alt text]({13E1E68A-D331-495B-8D71-0EA968F879B2}.png)

- Modifica i permessi del file per poterlo eseguire come programma:
![alt text]({109930FE-A0A0-4A99-A31E-3726DC64E589}.png)

- Avvia lo script appena creato:
![alt text]({0394C9EF-EC03-418E-AEE2-0FD2EF2118F5}.png)

### 6. Archiviazione e compressione di file

- Crea un archivio compresso contenente la cartella script utilizzando tar:
![alt text]({28A537B1-89BE-4328-8FFF-49E8F989FC6E}.png)

- Comprimi ulteriormente l’archivio generato con gzip:
![alt text]({DEE1091D-EDC5-4715-854E-8AF1EDB18C88}.png)

### 7. Verifica di processi e log di sistema

- Elenca tutti i processi in esecuzione nel sistema:
![alt text]({D0555763-67E5-4EB4-B8DD-9397F4B0B681}.png)

- Controlla i log di sistema (su Ubuntu il file si trova in /var/log/syslog, mentre in altre distribuzioni può essere in /var/log/messages o consultabile con journalctl):
![alt text]({C59D1EEF-3080-4898-8559-1F7AC11AF338}.png)

## 8. Controllo della rete

- Visualizza le schede di rete presenti nel sistema:
![alt text](image.png)

- Esegui un test di connessione verso un sito remoto, come google.com:
![alt text]({8FBAC21D-1418-4515-B857-8D6CC259F24F}.png)
 
## 9. Controllo dell’hardware e dei device files

- Mostra informazioni dettagliate sulla CPU in uso:
![alt text]({DBA2CCE0-C30C-4842-BB5C-132045F0FFB8}.png)

- Controlla lo stato della memoria RAM e il suo utilizzo attuale:
![alt text]({7045B8D2-69CE-478A-9C9B-C6E528F4AFD8}.png)

- Analizza la suddivisione dello spazio su disco:
![alt text]({63942F6E-C2C7-452C-8D2E-D43AD0B0A18C}.png)

- Verifica i dispositivi di archiviazione riconosciuti dal sistema:
![alt text]({8FEFC42C-44DC-4FB2-9161-877EA7904174}.png)











