import sqlite3
from Volo import *
from Hotel import *
from NoleggioAuto import *
from Passengers import * 
from DatabaseUtilties import *
from Controlli import *

conn = sqlite3.connect("GestionePrenotaViaggi.db")
cur = conn.cursor()
regVolo=Volo()
inserimentoDatiVoli()
inserimentoDatiHotel()

while True:
    scelta = input('''
    ========================================
    ==      0. Esci dal programma         ==
    ==      1. Registrare Voli            ==
    ==      2. Registrare Hotel           ==
    ==      3. Registrare Noleggi Auto    ==
    ==      4. Registrare Passeggeri      ==
    ==      5. Prenotare i Servizi        ==
    ========================================

    Scegli un'opzione: ''').strip()

    if scelta == "0":
        print("Arrivederci :)")
        break

    if scelta == "1":
        nome_compagnia = controlloNoNumeri("Inserisci il nome della compagnia: ")
        partenze = controlloNoNumeri("Inserisci il luogo di partenza: ")
        arrivi = controlloNoNumeri("Inserisci il luogo d'arrivo: ")
        prezzo = controlloNoLettere("Inserisci il prezzo: ")
        print("Volo registrato con successo")

    if scelta == "2":
        nome_hotel = controlloNoNumeri("inserisci il nome dell'hotel: ")
        luogo = controlloInizioNumeri("inserisci la città dove è situato: ")
        stelle = controlloNoLettere("inserisci quante stelle ha(numero da 1 a 5): ")
        room_num = controlloNoLettere ("inserisci il numero di stanze dell'hotel: ")
        room_type = controlloNoNumeri("inserisci il tipo di stanza: ")
        ##while True: scelta = input('''
        #
        #     0. Torna indietro         
        #     1. Standard            
        #     2. Lusso           
        #     3. Spa
        #     
        #   scegli un'opzione: '''

        #if scelta == "0":
        #    break
        #if scelta == "1":

        numeroTel = controlloNoLettere("inserisci il numero di telefono dell'hotel: ")
        #if 9 > numeroTel > 10 :
            #print("inserire un nuemero valido!")
        prezzo = controlloNoLettere("inserire il prezzo: ")
        print("Hotel registrato con successo!")


    if scelta == "3":
        nome_azienda = input("inserisci il nome dell'azienda di noleggi auto: ")
        #fare controlli su available = a quelli di room_num
        available_cars = input("inserisci le macchine disponibili: ")
        car_type = input("inserisci il tipo di macchina: ")#fai la scleta 1. economica 2. media 3. lusso
        targa = input("inserire la targa: ")
        prezzo = input ("inserisci il prezzo: ")
        print("Noleggio registrato!")

    if scelta == "4":
        nome = input("inserisci il nome: ")
        cognome = input("inserisci il cognome: ")
        email = input("inserisci la mail: ")
        numeroTel = input("inserisci il numero di telefono: ")
        print("Passeggero registrato")