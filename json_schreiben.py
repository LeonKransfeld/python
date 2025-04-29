import sys

datei = "haltestellen2.csv"

try:
    datei_lesen = open(datei, "r")
except:
    print("Datei nicht gefunden oder Probleme beim Öffnen")
    sys.exit()

haltestellen = datei_lesen.read()
print(haltestellen)
haltestellenListe = haltestellen.split("\n")

print(haltestellenListe)

sqlListe = []

for zeile in haltestellenListe:
    
    haltestelle = zeile.split(";")
    
#--------- ab hier Vorbereiten der Variablen (Liste) mit dictionarys 
#--------- zum schreiben als json-Datei
   

datei_lesen.close()
