import sqlite3
conn = sqlite3.connect("GestionePrenotaVisiteMediche.db")
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS Pazienti")
cur.execute('''
            CREATE TABLE IF NOT EXISTS Pazienti(
                id_paziente integer primary key autoincrement,
                nome TEXT,
                cognome TEXT,
                anno_nascita INTEGER
            )
            ''')

cur.execute("DROP TABLE IF EXISTS Medici")
cur.execute('''
            CREATE TABLE IF NOT EXISTS Medici(
                id_medico integer primary key autoincrement,
                nome TEXT,
                cognome TEXT
            )
            ''')

cur.execute("DROP TABLE IF EXISTS Visite")
cur.execute('''
            CREATE TABLE IF NOT EXISTS Visite(
                numeroVisita integer primary key autoincrement,
                giorno INTEGER,
                mese INTEGER,
                id_medico INTEGER,
                id_paziente INTEGER,
                foreign key (id_medico) REFERENCES Medico(id_medico)
                foreign key (id_paziente) REFERENCES Paziente(id_paziente)
            )
            ''')





conn.commit()

cur.close()
conn.close()
