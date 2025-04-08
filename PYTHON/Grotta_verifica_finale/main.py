import sqlite3
from Paziente import *
from Medico import *
from Visita import *
from DatabaseUtilties import *
from Controlli import *

conn = sqlite3.connect("GestionePrenotaVisiteMediche.db")
cur = conn.cursor()


registra_medici = Registra_medici()
organizza_visite = Organizza_visite()

while True: 
    scelta = (input('''
    0. Esci dal programma
    1. Registra Paziente
    2. Registra Medico
    3. Organizza visite

    Inserisci un'opzione : ''')).strip()


    if scelta == "0":
        print("Arrivederci <3")
        break

    elif scelta == "1":
        nome = controlloNoNumeri("Inserisci il nome del paziente: ")
        cognome = controlloNoNumeri("Inserisci il cognome del paziente: ")
        anno_nascita = controlloNoLettere("Inserire l'anno di nascita: ")
        Registra_pazienti.registraPazienti(nome, cognome, anno_nascita)
        print("\nPaziente registrato con successo!")

    elif scelta == "2":
        nome = controlloNoNumeri("Inserisci il nome del medico: ")
        cognome = controlloNoNumeri("Inserisci il cognome del medico: ")
        Registra_medici.registraMedici(nome, cognome)
        print("\nMedico registrato con successo!")


    elif scelta == "3":
        print(listaPazienti())
        id_paziente = controlloNoLettere("Inserisci l'id del paziente da visitare: ")
        print(listaMedici())
        id_medico = controlloNoLettere("Inserisci l'id del medico che effettuerà la visita: ")
        giorno = controlloNoLettere("Inserisci il giorno della visita: ")
        mese = controlloNoLettere("Inserisci il mese della visita: ")
        Organizza_visite.organizzaVisite(id_paziente, id_medico, giorno, mese)
        print("\nVisita prenotata!")
















    elif scelta == "883":
        print('''
        Come mai
        Ma chi sarai
        Per fare questo a me?
        Notti intere ad aspettarti
        Ad aspettare te
        Dimmi come mai
        Ma chi sarai
        Per farmi stare qui?
        Qui seduto in una stanza
        Pregando per un sì
        ''')
        break

    else:
        print("\nScegli una delle opzioni disponibli")
