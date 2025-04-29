def info():
    print("aufDictionaryPruefen(erstesDC, zweitesDC)")
    print("dictionaryEinfuegen(ganzesDC, teilDC)")
    print("dictionaryinDictionaryEinfuegen(ganzesDC, teilKey, teilDC)")    



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





    
    
    
