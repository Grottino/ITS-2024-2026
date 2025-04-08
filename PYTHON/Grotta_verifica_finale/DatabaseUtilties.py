import sqlite3
conn = sqlite3.connect("GestionePrenotaVisiteMediche.db")
cur = conn.cursor()

class Registra_pazienti:
    def registraPazienti(nome, cognome, data_nascita):
        cur.execute("INSERT INTO Pazienti(nome, cognome, anno_nascita) values (?,?,?)",(nome, cognome, data_nascita))
        conn.commit()

class Registra_medici:
    def registraMedici(nome, cognome):
        cur.execute("INSERT INTO Medici(nome, cognome) values (?,?)",(nome, cognome))
        conn.commit()

class Organizza_visite:
    def organizzaVisite(id_paziente, id_medico, giorno, mese):
        cur.execute("INSERT INTO Visite(id_paziente, id_medico, giorno, mese) values (?,?,?,?)",(id_paziente, id_medico, giorno, mese))
        conn.commit()

def listaPazienti() :
    
            lista_pazienti = list()

            result = cur.execute("select * from Pazienti")

            for row in result :
                lista_pazienti.append(row)

            return lista_pazienti

def listaMedici() :
    
            lista_medici = list()

            result = cur.execute("select * from Medici")

            for row in result :
                lista_medici.append(row)

            return lista_medici


