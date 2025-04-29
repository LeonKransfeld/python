import collections, threading
import mysql.connector, sys, time


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

class HaltestellenListe:  #enthält alle Haltestellen im Gebiet für viele Linien
    haltestellenliste=[]

    def add(self, haltestelle):
        #validieren: auf gültige Werte überprüfen, hier: Duplikate vermeiden
        self.haltestellenliste.append(haltestelle)
        self.haltestellenliste = list( set(self.haltestellenliste) )

    def remove(self, idhaltestelle):
        #alle Elemente (haltestelle) durchsuchen und auf Gleichheit der id überprüfen
        for aktuelleHaltestelle in self.haltestellenliste:
            if idhaltestelle == aktuelleHaltestelle.idhaltestelle:
                #wenn id gleich, dann aus der Liste entfernen und sofort beenden
                self. haltestellenliste.remove(aktuelleHaltestelle)
                break #oder return
    
    


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
   
    def __init__(self,kapazitaet, linie, fahrgastliste, aktuellePosition = 0, istFahrend = False):
        self.maxKapazitaet    = kapazitaet
        self.linie            = linie
        self.fahrgastliste    = fahrgastliste
        self.aktuellePosition = aktuellePosition
        self.istFahrend       = istFahrend
        
        if linie != None:
            self.linie         = linie.copy() # jedes Verkehrsmittel hat ein eigenes deque!
    pass
    
# Plan: linie aus der Datenbank laden
# was soll das Select zurückgeben?
# - fahrzeit
# - name der Von-Haltestelle
# - parameter: Name der Linie

                   #  z.B. "U35"
    def linieLaden(self, linienName):
        
        #Datenbankverbindung öffnen
        try:
            #self.divisionsfehler  = 7/0
            verbindung = mysql.connector.connect(host="localhost", user="root", password="")
            cursor = verbindung.cursor()

            cursor.execute("USE oepnv;")

            cursor.execute(f"""SELECT lsPosition, fahrzeit, haltestellenName
                               FROM linien_strecken as LS
                               JOIN strecken AS s
                               ON s.idStrecke = ls.idStrecke
                               JOIN haltestellen AS h
                               ON idHaltestelle = von
                               WHERE linienNummer = '{linienName}'
                               ORDER BY lsPosition ASC;""")

            
            # SELECT-statement senden

            self.linie = collections.deque()
            # das resultset lesen und im deque speichern
            for datensatz in cursor:
                self.linie.append(datensatz)  

            print(self.linie)

            cursor.close()

        except NameError as ne:
            print("Fehler bei Bezeichner")

        except mysql.connector.errors.InterfaceError:
            print("Datenbankserver nicht gefunden")
            sys.exit(0)  
            
        # für alle Exceptions:
        except BaseException as be:
            print("allgemeiner Fehler: ", type( be ) )
                  


# fahren() implementieren (thread)

    def fahren(self):
        #Indizes:
        self.aktuellerAnfang =  0
        self.haltestelle     =  2
        self.fahrzeit        =  1
        self.naechste        = -1
        
        while self.istFahrend == True:
            print(f"Angekommen an der Haltestelle {self.linie[self.aktuellerAnfang][self.haltestelle]}")
            time.sleep(self.linie[self.aktuellerAnfang][self.fahrzeit])
            self.linie.rotate(self.naechste)

# Zukunft: einsteigen und aussteigen der Fahrgäste...

    def losfahren(self):
        self.istFahrend = True
        self.fahrThread = threading.Thread(target=self.fahren)
        self.fahrThread.start()

    def anhalten(self):
        self.istFahrend = False        
        
    

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

#---- Laden aus der Datenbank testen ------------
              #kapazitaet, linie, fahrgastliste
hustadt = Strassenbahn(kapazitaet= 100, linie= None, fahrgastliste = None)
hustadt.linieLaden("U35")
#---- thread testen -----------------------------

hustadt.losfahren()
time.sleep(60)
hustadt.anhalten()
        
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


