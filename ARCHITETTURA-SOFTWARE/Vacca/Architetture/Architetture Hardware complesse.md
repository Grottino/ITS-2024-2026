Siamo arrivati a queste architetture per motivi storici.
1) Evoluzione dell'hardware data da una necessità di storage e velocità.
   Ad un certo punto si è capito che andava gestita in maniera centralizzata/automatizzata
2) Tendenze (Virtualizzazioni, Cloud, sicurezza, Affidabilità)
Esistono strumenti in grado di realizzare data center software definer

## NAS (Network attatch storage)
Il 1° sistema avanzato è l'oggetto NAS è un dispositivo collegato direttamente all'IP. Oltre al collegamento questi oggetti forniscono servizi sui file. Sono dei server che attacco ad una scheda di rete. I controller per i NAS sono dei Rade(Arrey ridondati di dischi indipendenti). Nei Nas ci sono anche dei software.
Con la rusbarry è possibile farti un NAS.
Utilizzano i protocolli FTP/IP.

#### Vantaggi:
- semplice implementazione
- Andiamo a Centralizzare per i file sistem
- I costi sono contenuti rispetto ad altre soluzioni di storage

#### Svantaggi:
- limiti del network ip su cui stiamo lavorando
- se la rete non è configurata bene possiamo avere dei colli di bottiglia
- non è adatto a tutte le applicazioni (in particolare a quelle applicaioni che hanno bisogno di accedere al disco in maniera più diretta avendo una velocità più alta)
#### Casi di utilizzo:
Condivisione di file in ufficio o piccole-medie imprese, archiviazione dei documenti dove facciamo backup, respository multimediali.
### SAN(Storage Area Network)
E' una rete dedicata allo storage separata dalla LAN principale che espone dispositivi di storage a livello di blocco. Vengono utilizzati con dei protocolli
Alcuni di questi: 
- ##### Fiber channel (alte prestazioni, bassa latenza, costose)
- ###### iSCSI (si legge "AISCASI") si appoggia al protocollo IP (come fosse Over IP) sfrutta infrastruttura già esistente e quindi costa meno
- ###### FCOE (Fiber Channel Over Ethernet) invece che fibra ottica. Utilizza protocolli FC ma li sfrutta usufruendo l'ethernet

## Storage Arrey
Un arrey di storage (di dischi veloci). Possono essere dischi magnetici, 
funzionalità di cash, snapshot, replica
switch in fiber channel o iscasi specializzati per gestire il traffico 
HDA una scheda di rete una nick specializzata
#### Vantaggi:
- alte prestazioni
- riduzione di colli di bottiglia
- supportare carichi di lavoro importanti
### Svantaggi:
- costo elevato 
- complessità di gestione
- competenze specialistiche (skill)
- richiede una struttura fisica dedicata

Casi uso esempio = data center di provider cloud

Servizi di failover = se mi fallisce qualcosa sono coperto

## Blade Server o Architetture a blocchi
Vengono alloggiati in uno Chassis (un contenitore, il case).
Alimentazione, raffreddamento, connettività sono caratteristiche delle architetture a blocchi.
##### Vantaggi:
- spazio ridotto 
- alta densità
- risparmio sulla corrente per l'alimentatore di grandezze maggiori
- strumenti centralizzati
##### Svantaggi:
- costi elevati (concentrazione termica, bisogno di elevato raffreddamento)
- possibilità di finire nel banned lock in

#### Componenti:
- Chassis (sciassì)
- Blade
- Schede di interfaccia

