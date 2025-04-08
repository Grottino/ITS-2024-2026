class Libro : 

    titolo=str()
    autore=str()
    editore=str()
    prezzo=float()
    id_biblioteca=int()

    def __init__(self,titolo,autore,editore,prezzo,id_biblioteca):
        self.titolo = titolo
        self.autore = autore     
        self.editore = editore
        self.prezzo = float(prezzo)
        self.id_biblioteca = int(id_biblioteca)


    