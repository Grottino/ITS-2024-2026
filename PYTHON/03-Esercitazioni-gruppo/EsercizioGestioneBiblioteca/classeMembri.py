class Membri :

    nome = str()
    cognome = str()
    id_biblioteca = int()
    data_nascita = str()
    email = str()

    def __init__(self,nome,cognome,id_biblioteca,email):
        self.nome = nome
        self.cognome = cognome
        self.id_biblioteca = int(id_biblioteca)
        self.email = email