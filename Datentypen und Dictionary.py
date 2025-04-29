# type()       Datentyp feststellen
# isinstance() auf Datentyp prüfen
# bisher: Liste, Set
# heute: Dictionary
# Umwandlung und Verschachtelung

# heute: Konvention der Bezeichner:  str???, i???, li???, dc???

strArtikel = 'USB Stick 16GB'
print( strArtikel, type(strArtikel) )

iAnzahl = 12
print( iAnzahl,    type(iAnzahl)    )

# key-value Paare
dcAnschrift = { "strasse":"Hauptstr", "hausNr":"1a", "plz":"01234", "ort":"Irgendwo" }

       
dcPerson    = { "vorname":"Frank", "nachname":"Kraft"}
print(dcPerson, type( dcPerson)    )

#man kann auf einen erwarteten Datentyp mit isinstance prüfen!
#Funktionen können vorab prüfen, ob der übergebene Parameter "passt"
if isinstance(strArtikel, dict):
    print( "strArtikel ist vom Datentyp dictionary")
else:
    print( "strArtikel ist vom Datentyp ", type(strArtikel) )

# Versuch ein dictionary in ein anderes dictionary verschachteln!
#Idee: eine ähnliche Struktur wie unter JSON zu bilden

def aufDictionaryPruefen(erstesDC, zweitesDC):
    #Validierung - prüfung auf gültige Parameter
    if not isinstance(erstesDC, dict):
        return False
    if not isinstance(zweitesDC,   dict):
        return False
    return True


def dictionaryEinfuegen(ganzesDC, teilDC):
    #Validierung - prüfung auf gültige Parameter
    #DRY - don't repeat yourself, deshalb Funktion definieren und mehrfach aufrufen
    if aufDictionaryPruefen(ganzesDC, teilDC) == True:

       ganzesDC.update(teilDC)
       return True
    return False

# Pfadabdeckung 100%
# 1. Test: das Ganze ist kein DC
# 2. Test: das Teil  ist kein DC
# 3. Einfügen wird durchgeführt

tFehler= "Test nicht bestanden"
tErfolg= "Test bestanden"

if dictionaryEinfuegen(iAnzahl, dcAnschrift) == True:
    print("1. ", tFehler)
else:
    print("1. ", tErfolg)

if dictionaryEinfuegen(dcPerson, strArtikel) == True:
    print("2. ", tFehler)
else:
    print("2. ", tErfolg)

    
if dictionaryEinfuegen(dcPerson, dcAnschrift) == False:
    print("3. ", tFehler)
else:
    print("3. ", tErfolg)


dcPerson["anschrift"] = None
print(dcPerson)
del dcPerson["anschrift"]

def dictionaryinDictionaryEinfuegen(ganzesDC, teilKey, teilDC):
    # zusätzlich: neuen key einfügen
    # diesem key das dictionary zuweisen

    if not aufDictionaryPruefen(ganzesDC, teilDC):
        return False
    
    # Validierung des neuen Schlüssels:
    # muss str sein
    # darf nicht bereits existieren
    # kein leerer str   also nicht:   "": "eine Information"

    if not type( teilKey) == str:
        return False
    if len(teilKey) == 0:
        return False

    schluessel = ganzesDC.keys()
    if teilKey in schluessel:
        return False

    # Tests positiv absolviert
    
    ganzesDC[teilKey] = teilDC

#---------------------------------------------------

dictionaryinDictionaryEinfuegen(dcPerson, "anschrift", dcAnschrift)

print(dcPerson)



    
    
    
