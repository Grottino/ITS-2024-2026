class Prodotto :

    __nome = str()
    __prezzo = float()

    def __init__(self,nome,prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def getNome(self) :
        return self.nome
    
    def getPrezzo(self) :
        return self.prezzo



class Cliente :

    __nome = str()
    __cognome = str()
    __email = str()
    __numero = str()


    def __init__(self,nome,cognome,email,numero):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.numero = numero

    def getNome(self) :
        return self.nome
    
    def getCognome(self) :
        return self.cognome 

    def getEmail(self) :
        return self.email
    
    def getNumero(self) :
        return self.numero