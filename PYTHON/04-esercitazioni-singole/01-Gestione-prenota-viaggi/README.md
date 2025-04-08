## Gestione Sistema di prenotazione di viaggi

#### come prima cosa creo 7 sorgenti chiamate rispettivamente: Volo, Hotel, AutoNoleggio, Passeggero, DatabaseUtilities, main, dump.py.

### creo il db e lo popolo:
Volo:
- id_volo
- nome compagnia
- partenze
- arrivi
- prezzo

Hotel:
- id_hotel
- nome hotel
- luogo(fai che quando viene selezionato il volo verso quel luogo chiede se vuole prenotare anche l'hotel)
- stelle (da 3 a 5)
- numero stanze (room_num)
- tipi di stanze[room_type] (standard, lusso, spa)
- numeroTel
- prezzo

Noleggi auto:
- id_noleggio
- nome azienda noleggi (nome_azienda)
- macchine disponibili (available_cars)
- categoria auto [car_type](economica, media, lusso)
- targa
- prezzo

passeggero:
- id_utente
- nome
- cognome
- email
- numeroTel

### creo le sorgenti: (incluse quelle riportate sopra)

DatabaseUtilities:
- funzioni utili a non ripetere le righe di codice
- controlli 

Main
File prinicale di scrittura dove verrà eseguito il codice:
- importare tutti i file (from nome import *)
- fare gli insert
- menù
- scelte

### esegui i vari controlli:
- try except(except Exception as e)
- controllo vuoto
- controllo no numeri
- controllo no lettere
- controllo no simboli(opzionale)
