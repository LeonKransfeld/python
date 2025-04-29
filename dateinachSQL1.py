import sys

dateiEin = "partie.txt"
dateiAus = "partie.sql"

try:
    #eine im Betriebssystem festgelegte Referenz auf eine geöffnete Datei
    handleIn  = open(dateiEin, "r")
    handleOut = open(dateiAus, "w")
except:
    print("Datei nicht gefunden oder Probleme beim Öffnen")
    sys.exit()

#Datentyp wird auf String festgelegt:
zuege = ""

zeile = handleIn.readline()
#enthält z.B. [Event "IBM Kasparov vs. Deep Blue Rematch"]
while zeile:
    #if(erstes Zeichen == "["
    if zeile[0]=="[":
        liste = zeile.split("\"")
        #Inhalt:
        #[Event
        #IBM Kasparov vs. Deep Blue Rematch
        #]
        key   =  liste[0]
        #erstes Zeichen entfernen:
        key   = key[1:]
        value =  liste[1]

        print(          f"INSERT INTO metadaten VALUES (\"{key}\", \"{value}\" );" )
        handleOut.write(f"INSERT INTO metadaten VALUES (\"{key}\", \"{value}\" );")
        handleOut.write("\n")
    else:
        zuege = zuege + zeile.replace("\n", "")
    zeile = handleIn.readline()

handleIn.close()
handleOut.close()

zugListe = zuege.split()
zugSQL   = "INSERT INTO halbzuege VALUES "
naechsterZugSchreiben = False
zugZaehler = 0

for aktuellesElement in zugListe:
    #nächsten Eintrag mit "??." suchen, ignorieren
    if aktuellesElement[-1] == ".":
        naechsterZugSchreiben = True
        continue
    zugSQL = zugSQL + f"( {zugZaehler}, '{aktuellesElement}'),"    
    #zugzähler um 1 erhöhen
    #die zwei darauffolgenden Einträge speichern

print(zugListe)
