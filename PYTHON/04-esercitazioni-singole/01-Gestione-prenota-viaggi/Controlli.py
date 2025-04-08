import re 

def controlloVuoto(stringa="") : 
    while True :
        controllo=input(stringa).lower().strip()
        if controllo=="":
            print("Non lasciare il campo vuoto")
        else :
            return controllo
        
def controlloNoNumeri(stringa="") : 
    while True :
        controllo=input(stringa)
        controllo=controllo.lower().strip()
        if controllo=="":
            print("Non lasciare il campo vuoto")
        elif re.findall('[0-9]',controllo) :
            print("Non puoi inserire numeri")
        else :
            return controllo
        
def controlloNoLettere(stringa="") : 
    while True :
        controllo=input(stringa).lower().strip()
        if controllo=="":
            print("Non lasciare il campo vuoto")
        elif re.findall('\D',controllo) :
            print("Non puoi inserire lettere")
        else :
            return controllo
        
def controlloVuotoMail(stringa="") : 
    while True :
        controllo=input(stringa).lower().strip()
        if controllo=="":
            print("Non lasciare il campo vuoto")
        elif re.findall('@',controllo) :
            return controllo
        else :
            print("Non è una mail valida")

def controlloInizioNumeri(stringa="") : 
    while True :
        controllo=input(stringa).lower().strip()
        if controllo=="":
            print("Non lasciare il campo vuoto")
        elif re.findall('^[0-9]',controllo) :
            print("Non può iniziare con un numero")
        else :
            return controllo