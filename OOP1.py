class Fahrgast:

    #Methoden
    def warten(haltestelle):
        pass
    
    def einsteigen():
        pass
    
    def aussteigen():
        pass

    def __init__(self, idfahrgast, vorname, nachname, vonHaltestelle, nachHaltestelle):
        #ist das eine Integer? 
        self.fahrgastid      = idfahrgast
        self.vorname         = vorname
        self.nachname        = nachname
        #ist das eine Integer?
        self.vonHaltestelle  = vonHaltestelle
        #ist das eine Integer?
        self.nachHaltestelle = nachHaltestelle

    def __str__():
        pass

class Haltestelle:
    #Liste der wartenden Fahrgäste
    
    def fahrgastHinzufuegen(self, fahrgast):
        self.fahrgastliste.append(fahrgast)
        
    def fahrgastEntfernen(self, fahrgast):
        try:
            self.fahrgastliste.remove(fahrgast)
            return True
        except:
            return False
        
    def __str__():
        for aktuellerFahrgast in self.fahrgastliste:
            print(aktuellerFahrgast)
        
        pass

class Omnibus:
    pass
  
        
        
#----Objekte erzeugen--------------------------------------------------------

karlheinz = Fahrgast(1, 'Karlheinz', 'Koslowski', 666, 999)
maria     = Fahrgast(2, 'Maria',     'Krohn',     123, 321)

# implementiere die Methode __init()__ der Klasse Haltestelle
# implementiere die Methode __str__() der Klasse Fahrgast


