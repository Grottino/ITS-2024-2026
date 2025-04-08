import sqlite3

conn = sqlite3.connect("GestioneBiblioteca.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Biblioteche")

cur.execute('''

            CREATE TABLE IF NOT EXISTS Biblioteche(
            
                id_biblioteca integer primary key autoincrement,
                nome TEXT,
                via TEXT,
                citta TEXT,
                telefono TEXT

            )

''')

cur.execute("DROP TABLE IF EXISTS Libri")

cur.execute('''

            CREATE TABLE IF NOT EXISTS Libri(
            
                id_libro integer primary key autoincrement,
                titolo TEXT,
                autore TEXT,
                editore TEXT,
                prezzo REAL,
                id_biblioteca INTEGER,
                prestito int,
                FOREIGN KEY (id_biblioteca) REFERENCES Biblioteche(id_biblioteca)
                FOREIGN KEY (prestito) REFERENCES Membri(id_membro)

            )

''')

cur.execute("DROP TABLE IF EXISTS Membri")

cur.execute('''

            CREATE TABLE IF NOT EXISTS Membri(
            
                id_membro integer primary key autoincrement,
                nome TEXT,
                cognome TEXT,
                id_biblioteca INTEGER,
                email TEXT,
                FOREIGN KEY (id_biblioteca) REFERENCES Biblioteche(id_biblioteca)

            )

''')

conn.commit()

cur.close()
conn.close()


