import sqlite3

def getCursor() :
    conn = sqlite3.connect("gestioneElettronica.db")
    cur = conn.cursor()
    return cur,conn

def execCursor(query,dato=None) :
    asd = getCursor()
    cur=asd[0]
    conn=asd[1]
    if dato==None :
        return cur.execute(query)
    else : 
        cur.execute(query,dato)
        conn.commit()

def listaProdotti() :

    lista_prodotti=list()

    result = execCursor("select * from prodotti")

    for row in result :
        lista_prodotti.append(row)

    return lista_prodotti


def richiestaQuantità(stringa1,stringa2) :
    quantità=input(stringa2)
    prodotto_scelto=input(stringa1)
    return prodotto_scelto, quantità

def richiestaId(stringa) :
    prodotto_scelto=controlloVuoto("Inserisci l'id ")
    return prodotto_scelto

def controlloVuoto(string) :

    risultato=input(string)
    
    risultato=risultato.lower().strip()

    if risultato == "":
        print("Non puoi inserire un valore vuoto")
    else :
        return risultato



