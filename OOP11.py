import collections, threading

class Fahrgast:

    #Methoden
    def warten(self, haltestelle):
        pass
    
    def einsteigen(self, nahverkehrsmittel ):
        pass
    
    def aussteigen(self, nahverkehrsmittel ):
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
        print(self.__dict__)

    def getFahrgastid(self):
        return self.fahrgastid
    def getVorname(self):
        return self.vorname
    def getNachname(self):
        return self.nachname

class Haltestelle:
    
    def __init__(self, idhaltestelle, haltestellenname):
        self.idhaltestelle    = idhaltestelle
        self.haltestellenname = haltestellenname
        self.fahrgastliste = []
        

    
    def fahrgastHinzufuegen(self, fahrgast):
        if fahrgast.vonHaltestelle == self.idhaltestelle:
            self.fahrgastliste.append(fahrgast)
            return True
        else:
            return False
        
    def fahrgastEntfernen(self, fahrgast):
        try:
            self.fahrgastliste.remove(fahrgast)
            return True
        except:
            return False
        
    def __str__(self):
        #print(self.__dict__)
        #for aktuellerFahrgast in self.fahrgastliste:
        #    print(aktuellerFahrgast)
        returnString = f"ID: {self.idhaltestelle} Name: {self.haltestellenname}" + '\n'
        for aktuellerFahrgast in self.fahrgastliste:
            returnString += f"ID: {aktuellerFahrgast.getFahrgastid()} Vorname: {aktuellerFahrgast.getVorname()} Nachname: {aktuellerFahrgast.getNachname()} \n"
        return returnString

class Strecke:
    def __init__(self, vonHaltestelle, bisHaltestelle, fahrzeit):
        #Attribut des Objektes erhält Parameter des Aufrufs
        self.vonHaltestelle   = vonHaltestelle
        self.bisHaltestelle   = bisHaltestelle
        self.fahrzeit         = fahrzeit  

    def getVonHaltestelle(self):
         return self.vonHaltestelle

    def getBisHaltestelle(self):
         return self.bisHaltestelle

    def getFahrzeit(self):
         return self.fahrzeit

    def info(self):
         print( "getVonHaltestelle() \n  getBisHaltestelle() \n getFahrzeit()")
         
    
class Linie:
    strecken    = collections.deque()
    linienNummer = None

    def add(self, strecke):
        #Validierung: ist das wirklich ein Strecken-Objekt?
        if type(strecke) != '__main__.Strecke':
            return
        #ist die zuletzt angefahrene Haltestelle mit der neuen vonHaltestelle identisch?
        if self.strecken[  len( self.strecken) - 1 ].getBisHaltestelle() == strecke.getVonHaltestelle():
            self.strecken.append(strecke)
        

           
        #print( type(strecke)  )        

class Nahverkehrsmittel:
    maxKapazitaet = 0
    linie         = None # Liste von Haltestellen, unsortiert
    fahrgastliste = []
    aktuellePosition = 0

    def __init__(self,kapazitaet, linie):
        self.maxKapazitaet = kapazitaet
        self.linie         = linie.copy() # jedes Verkehrsmittel hat ein eigenes deque!
    pass
    

class Omnibus(Nahverkehrsmittel):
    pass
class Strassenbahn(Nahverkehrsmittel):
    pass
        
#---- Strecke und Linie testen ------------------

aNachB    = Strecke(123, 234, 4)
cNachD    = Strecke( 15,   2, 6)
Stadtbahn = Linie()
Stadtbahn.add(aNachB)
Stadtbahn.add(cNachD)

        
#----Objekte erzeugen--------------------------------------------------------

haltestelleBahnhof         = Haltestelle(666, 'Hauptbahnhof')
haltestelleAnderaltenEiche = Haltestelle(999, 'An der alten Eiche')
haltestelleAmMarkt         = Haltestelle(321, 'Am Markt')
haltestelleFriedrich       = Haltestelle(123, 'Friedrich-Schiller-Str') 

karlheinz = Fahrgast(1, 'Karlheinz', 'Koslowski', 666, 999)
maria     = Fahrgast(2, 'Maria',     'Krohn',     123, 321)

haltestelleBahnhof.fahrgastHinzufuegen(karlheinz)
haltestelleFriedrich.fahrgastHinzufuegen(maria)

#TEst: funktioniert die Validierung?
haltestelleFriedrich.fahrgastHinzufuegen(karlheinz)
                                          
print(haltestelleBahnhof)
print(haltestelleFriedrich)

# implementiere die Methode __init()__ der Klasse Haltestelle
# implementiere die Methode __str__() der Klasse Fahrgast


