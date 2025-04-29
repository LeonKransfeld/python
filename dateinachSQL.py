import sys

datei = "partie.txt"

try:
    #eine im Betriebssystem festgelegte Referenz auf eine geöffnete Datei
    handle = open(datei)
except:
    print("Datei nicht gefunden")
    sys.exit()


zeile = handle.readline()
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

        print( f"INSERT INTO metadaten VALUES (\"{key}\", \"{value}\" );" )
    
    zeile = handle.readline()

handle.close()
