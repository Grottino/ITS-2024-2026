import sqlite3
conn = sqlite3.connect("GestionePrenotaViaggi.db")
cur = conn.cursor()

def inserimentoDatiVoli(oggetto):
    cur.execute("INSERT INTO Voli (id_volo, nome_compagnia, partenze, arrivi, prezzo) values (?,?,?,?,?)", (oggetto.nome_compagnia, oggetto.partenze, oggetto.arrivi, oggetto.prezzo))
    conn.commit()

def inserimentoDatiHotel(oggetto):
    cur.execute("INSERT INTO Hotel (id_hotel, nome_hotel, luogo, stelle, room_num, room_type, numeroTel, prezzo) values (?,?,?,?,?,?,?,?)", (oggetto.id_hotel, oggetto.nome_hotel, oggetto.luogo, oggetto.stelle, oggetto.room_num, oggetto.room_type, oggetto.numeroTel, oggetto.prezzo))
    conn.commit()


