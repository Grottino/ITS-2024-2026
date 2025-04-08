import sqlite3

conn = sqlite3.connect("GestionePrenotaViaggi.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Voli")
try:
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Voli(

                    id_volo integer primary key autoincrement,
                    nome_compagnia TEXT not null,
                    partenze TEXT not null,
                    arrivi TEXT not null,
                    prezzo real
                )
    ''')

    cur.execute("DROP TABLE IF EXISTS Hotel")

    cur.execute('''
                CREATE TABLE IF NOT EXISTS Hotel(

                    id_hotel integer primary key autoincrement,
                    nome_hotel TEXT not null,
                    luogo TEXT not null,
                    stelle INTEGER,
                    room_num INTEGER,
                    room_type TEXT not null,
                    numeroTel INTEGER not null,
                    prezzo real
                )
    ''')

    cur.execute("DROP TABLE IF EXISTS NoleggiAuto")

    cur.execute('''
                CREATE TABLE IF NOT EXISTS NoleggiAuto(
                    
                    id_noleggio integer primary key autoincrement,
                    nome_azienda TEXT not null,
                    available_cars INTEGER,
                    car_type TEXT not null,
                    targa TEXT not null,
                    prezzo real
                )
    ''')

    cur.execute("DROP TABLE IF EXISTS Passeggeri")

    cur.execute('''
                CREATE TABLE IF NOT EXISTS Passeggeri(
                
                id_utente integer primary key autoincrement,
                nome TEXT not null,
                cognome TEXT not null,
                email TEXT not null,
                numeoTel INTEGER not null
                )
    ''')

    conn.commit()
except:
    print("qualcosa è andato storto")
cur.close()
conn.close()