import sqlite3

conn = sqlite3.connect("gestioneElettronica.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS prodotti")

cur.execute(''' CREATE TABLE IF NOT EXISTS prodotti(
            
                id_prodotto integer primary key autoincrement,
                nome TEXT,
                prezzo REAL,
                quantità integer DEFAULT 0
            
            )''')

cur.execute("DROP TABLE IF EXISTS clienti")

cur.execute(''' CREATE TABLE IF NOT EXISTS clienti(
            
                id_cliente integer primary key autoincrement,
                nome text,
                cognome text,
                email text,
                numero text
            
            )''')

conn.commit()

cur.close()
conn.close()
