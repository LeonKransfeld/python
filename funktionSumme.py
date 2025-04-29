# Funktionen schreiben

#Funktionen strukturieren den Code
#Funktionen eignen sich, wiederholt Anweisungsblöcke auszuführen
#Programmierparadigma: DRY (don't repeat yourself)
#Parameter sind die Eingabewerte einer Funktion
#später, in der objektorientierten Umgebung (Klassen) stellen Funktionen einen wesentlich Teil dar
# die Funktionen werden dann Methoden genannt
#zusammen mit den Variablen, die dann Atribute heißen, bilden diese Klassen (Schablonen für Objekte)



def summe(zahl1, zahl2):
    addiert = zahl1 + zahl2
    return addiert

dutzend = 12
hundert = 100


def summeviele(*zahlen):
    len(zahlen)
    aktuelleSumme = 0
    for aktuelleZahl in zahlen: 
      aktuelleSumme += aktuelleZahl
#     aktuelleSumme = aktuelleSumme + aktuelleZahl

    return aktuelleSumme

#def fibonacci(anzahl):
    
#Funktionen mit Vorgabewerten: Wenn kein Parameter übergeben wird, wird der vordefinierte Wert übernommen
def vorgabewerte(zahl = 1):
    return zahl * zahl

#call-by-value, call-by-reference
def tanken(menge, tank, diesel= False):
    if diesel == True:
       tank = tank + menge
       return True
    else:   
       return False

ergebnis = summe(dutzend, hundert)
print(dutzend, "+",hundert, "=", ergebnis)

summequadrat = summeviele(1,4,9,16)
print("die Summe der Quadratzahlen bis 16 ergibt", summequadrat)

quadrat = vorgabewerte(5)
print("Das quadrat von 5 ist ", quadrat)

quadrat = vorgabewerte()
print("Der Vorgabewert 1 wurde genutzt: ", quadrat)

tankvolumen = 30.0
tankinhalt  = 25.5

tanken(tankvolumen, tankinhalt, True)

print("der Tankinhalt ist jetzt ", tankinhalt)

#Aufgabe: erstelle die Funktion fibonacci(anzahl)
#die Funktion soll zunächst die berechneten Zahlen nur mit print() ausgeben

#weitere Aufgabe: erstelle eine Funktion, welche die Eulersche Zahl in Näherung berechnet:
#                 1 + 1/2 + 1/3 + 1/4 +......
# euler(zahl) 

#Die Fakultät einer Zahl entsteht durch fortlaufendes Multiplizieren mit der um 1 reduzierten Zahl, bis 1 erreicht ist.
#6! = 6 x 5 x 4 x 3 x 2 x 1
#Erstelle die Funktion fakultät(zahl), welche dieses Produkt zurückgibt.(while)




