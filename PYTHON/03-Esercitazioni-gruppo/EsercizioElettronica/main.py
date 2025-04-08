import sqlite3
from classiElettronica import *
from funzioni import *

def listaClienti() :
    
    lista_clienti = list()

    result = execCursor("select * from clienti")

    for row in result :
        lista_clienti.append(row)

    return lista_clienti
    
def inserimentoProdotto(prodotto) :

    execCursor("insert into prodotti (nome, prezzo) values (?,?)", (prodotto.getNome(), prodotto.getPrezzo()))


def inserimentoCliente(cliente) :

    execCursor("insert into clienti (nome,cognome,email,numero) values (?,?,?,?)", (cliente.getNome(), cliente.getCognome(), cliente.getEmail(), cliente.getNumero()))

while True :
    # Visualizzazione menù
    print('''

        0. Esci
        1. Gestisci Prodotti
        2. Gestisci Clienti

    ''')

    scelta=input("Opzione : ")

    scelta=scelta.strip()

    if scelta == "0" :
        print("Sei uscito ! ")
        break

    elif scelta == "1" : 

        while True :

            print('''

                0. Indietro
                1. Inserisci Prodotto
                2. Aggiungi Quantità Prodotto
                3. Rimuovi Quantità Prodotto
                4. Visualizza Lista Prodotti

            ''')

            scelta=input("Opzione : ")

            scelta=scelta.strip()

            if scelta == "0" :

                break

            elif scelta == "1" :

                nome_prodotto=controlloVuoto("Inserire il nome del prodotto da aggiungere : ")
                prezzo_prodotto=controlloVuoto("Inserisci il prezzo del prodotto : ")

                prodotto = Prodotto(nome_prodotto,prezzo_prodotto)

                inserimentoProdotto(prodotto)

            elif scelta == "2" :

                print(listaProdotti())

                execCursor("update prodotti set quantità = quantità + (?) where id_prodotto=(?)", richiestaQuantità("Inserisci la quantità da aggiungere ","Inserisci l'id del prodotto "))

                continue
            elif scelta == "3":

                print(listaProdotti())

                execCursor("update prodotti set quantità = quantità + -(?) where id_prodotto=(?)", richiestaQuantità("Inserisci la quantità da rimuovere ","Inserisci l'id del prodotto "))

            elif scelta == "4":

                print(listaProdotti())

            else :

                print("Scegli un'opzione disponibile")

    elif scelta == "2" : 

        while True :

            print('''

                0. Indietro
                1. Inserisci Cliente
                2. Visualizza Lista Clienti

            ''')

            scelta=input("Opzione : ")

            scelta=scelta.strip()

            if scelta == "0" :

                break

            elif scelta == "1" :

                nome_cliente=controlloVuoto("Inserire il nome del cliente da aggiungere : ")
                cognome_cliente=controlloVuoto("Inserire il cognome del cliente da aggiungere : ")
                email_cliente=controlloVuoto("Inserire l'email del cliente da aggiungere : ")
                numero_cliente=controlloVuoto("Inserire il numero del cliente da aggiungere : ")

                cliente = Cliente(nome_cliente,cognome_cliente,email_cliente,numero_cliente)

                inserimentoCliente(cliente)

            if scelta == "2" :

                print(listaClienti())

                execCursor("delete from clienti where id_cliente = (?)", controlloVuoto())

            else :

                print("Scegli un'opzione disponibile")

    else :

        print("Scegli un'opzione disponibile")

    