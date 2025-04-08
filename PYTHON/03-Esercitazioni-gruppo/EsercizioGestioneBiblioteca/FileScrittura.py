from classeLibri import Libro
from classeMembri import Membri
from classeBiblioteche import Biblioteche
import sqlite3
from Funzioni import *

conn = sqlite3.connect("GestioneBiblioteca.db")
cur = conn.cursor()

def inserimentoLibri(oggetto) :
    
    cur.execute("INSERT INTO libri(titolo,autore,editore,prezzo,id_biblioteca) values (?,?,?,?,?)",(oggetto.titolo, oggetto.autore, oggetto.editore, oggetto.prezzo, oggetto.id_biblioteca))
    conn.commit()
    
def inserimentoMembri(oggetto) :

    cur.execute("INSERT INTO membri(nome,cognome,id_biblioteca,email) values (?,?,?,?)",(oggetto.nome, oggetto.cognome, oggetto.id_biblioteca, oggetto.email))
    conn.commit()

def inserimentoBiblioteche(oggetto) :

    cur.execute("INSERT INTO biblioteche(nome,via,citta,telefono) values (?,?,?,?)",(oggetto.nome, oggetto.via, oggetto.citta, oggetto.telefono))
    conn.commit()

def prestitoLibro(id_user,id_libro) :

    cur.execute("update libri set prestito = ? where id_libro = ?",(id_user,id_libro))
    conn.commit()

def restituzioneLibro(id_libro) :

    cur.execute("update libri set prestito = NULL where id_libro = ?",(id_libro))
    conn.commit()

def bibliotecheDisponibili():

    lista_biblioteche=list()
    lista=""

    result=cur.execute("select * from biblioteche ")
    for row in result :
        print(row)
        lista_biblioteche.append((row[1],str(row[0])))

    for x in lista_biblioteche:
        lista+=x[0]+" "+x[1]+" , "
    
    lista=lista.rstrip(", ")
    
    return lista,lista_biblioteche

def libriDisponibili():

    lista_libri=list()
    lista=""

    result=cur.execute("select * from libri where prestito is null")
    for row in result :
        lista_libri.append((row[1],str(row[0]),str(row[5])))

    for x in lista_libri:
        lista+=" ||| NOME : " + x[0]+ " ||| ID LIBRO : "+x[1] + " ||| BIBLIOTECA " + x[2] +  " ||| \n "
    
    return lista,lista_libri

def usersDisponibili():

    lista_users=list()
    lista=""

    result=cur.execute("select * from membri")
    for row in result :
        lista_users.append((row[1],str(row[0])))

    for x in lista_users:
        lista+= "||| NOME " + x[0]+" ||| ID UTENTE :"+x[1] + " ||| \n "
    
    return lista,lista_users

def libriNonDisponibili():

    lista_libri=list()
    lista=""


    result=cur.execute("select libri.id_libro, libri.titolo, membri.nome from libri join membri on libri.prestito = membri.id_membro where prestito is not null")
    for row in result :
        lista_libri.append((row[1],str(row[0]),str(row[2])))

    for x in lista_libri:
        lista+="||| NOME LIBRO " + x[0]+" ||| ID LIBRO "+x[1]+" ||| PRESO IN PRESTITO DALL'UTENTE:  " + x[2] + " ||| \n "
    
    return lista,lista_libri
    
while True :
    scelta=(input('''
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                
    ++++                                                  ++++
    ++++                    BENVENUTO                     ++++
    ++++                                                  ++++
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ++++                                                  ++++
    ++++            0. Per uscire                         ++++
    ++++            1. Per aggiungere un libro            ++++          
    ++++            2. Per registrare un nuovo membro     ++++
    ++++            3. Per prestare un libro              ++++                  
    ++++            4. Per restituire un libro            ++++                
    ++++            5. Per aggiungere una biblioteca      ++++
    ++++                                                  ++++
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                 
    
    Inserisci un'opzione : ''')).strip()


    if scelta == "0" :

        print("Alla prossima :D")
        cur.close()
        conn.close()
        break

    elif scelta == "1":
        
        
        listaBibliotecheDisponibili = list()

        for row in bibliotecheDisponibili()[1] :
            listaBibliotecheDisponibili.append(row[1])
        
        if len(listaBibliotecheDisponibili) == 0 :
            print("NON ESISTE NESSUNA BIBLIOTECA")
            continue

        
        titolo=controlloVuoto("Inserisci il titolo : ")
        autore=controlloVuotoNumeri("Inserisci un autore : ")
        editore=controlloVuotoNumeri("Inserisci editore : ")
        prezzo=controlloVuotoLettere("Inserisci il prezzo : ")

        while True :
            print("Lista di biblioteche disponibili con il loro nome e id : \n", (bibliotecheDisponibili()[0]))
            id_biblioteca=controlloVuotoLettere("Inserisci l'id della biblioteca : ")
            if id_biblioteca in listaBibliotecheDisponibili :
                break
            else :
                print("!!!Scegli una biblioteca disponibile !!!")

        libro_inserimento=Libro(titolo,autore,editore,prezzo,id_biblioteca)
        inserimentoLibri(libro_inserimento)
        print("Libro aggiunto correttamente!")

    elif scelta == "2":

        listaBibliotecheDisponibili = list()

        for row in bibliotecheDisponibili()[1] :
            listaBibliotecheDisponibili.append(row[1])

        if len(listaBibliotecheDisponibili) == 0 :
            print("NON ESISTE NESSUNA BIBLIOTECA")
            continue

        nome=controlloVuotoNumeri("Inserisci il nome : ")
        cognome=controlloVuotoNumeri("Inserisci il cognome : ")

        while True :
            print("Lista di biblioteche disponibili con il loro nome e id : \n", (bibliotecheDisponibili()[0]))
            id_biblioteca=controlloVuotoLettere("Inserisci l'id della biblioteca : ")
            if id_biblioteca in listaBibliotecheDisponibili :
                break
            else :
                print("!!!Scegli una biblioteca disponibile !!!")

        email=controlloVuotoMail("Inserisci la tua email : ")
        membro_inserimento=Membri(nome,cognome,id_biblioteca,email)
        inserimentoMembri(membro_inserimento)
        print("Membro registrato con successo!")

    elif scelta == "3":
        
        listaLibriDisponibili=list()
        listaMembriDisponibili=list()

        for row in libriDisponibili()[1] :
            listaLibriDisponibili.append(row[1])

        if len(listaLibriDisponibili) == 0 :
            print("NON ESISTE NESSUN LIBRO DISPONIBILE")
            continue

        for row in usersDisponibili()[1] :
            listaMembriDisponibili.append(row[1])

        if len(listaMembriDisponibili) == 0 :
            print("NON ESISTE NESSUN MEMBRO")
            continue

        while True :
            print("Lista di libri disponibili con il loro loro nome, id e id della biblioteca : \n",libriDisponibili()[0])
            id_libro=controlloVuotoLettere("Inserisci l'id del libro da prestare: ")
            if id_libro in listaLibriDisponibili :
                break
            else :
                print("!!! Scegli un libro disponibile !!!")

        while True :
            print("Lista di membri disponibili : \n", (usersDisponibili()[0]))
            id_membro=controlloVuotoLettere("Inserisci l'id del utente a quale vuoi prestare : \n")
            if id_membro in listaMembriDisponibili :
                break
            else :
                print("!!!Scegli una membro disponibile !!!")

        prestitoLibro(id_membro,id_libro)
        print("Buona lettura!")

    elif scelta == "4":

        listaLibriNonDisponibili=list()

        for row in libriNonDisponibili()[1] :
            listaLibriNonDisponibili.append(row[1])

        if len(listaLibriNonDisponibili) == 0 :
            print("NON ESISTE NESSUN LIBRO PRESTATO")
            continue

        while True :
            print("Lista di libri prestati con il loro nome, id e id della biblioteca : \n",libriNonDisponibili()[0])
            id_libro=controlloVuotoLettere("Quale libro vuoi restituire? : ")
            if id_libro in listaLibriNonDisponibili :
                break
            else :
                print("Scegli un libro disponibile ")

        restituzioneLibro(id_libro)
        print("Libro restituito con successo")
    elif scelta == "5":

        nome_biblioteca=controlloInizioNumeri("Inserisci il nome della biblioteca : ")
        via_biblioteca=controlloInizioNumeri("Inserisci la via della biblioteca : ")
        citta_biblioteca=controlloVuotoNumeri("Inserisci la citta' della biblioteca : ")
        telefono_biblioteca=controlloVuotoLettere("Inserisci il numero della biblioteca : ")
        biblioteca_inserimento=Biblioteche(nome_biblioteca, via_biblioteca, citta_biblioteca, telefono_biblioteca)
        inserimentoBiblioteche(biblioteca_inserimento)
        print("Biblioteca aggiunta")

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
    else :

        print("Scegli una delle opzioni disponibli")
    



