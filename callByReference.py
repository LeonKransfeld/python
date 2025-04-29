def tankenMitListe(menge, inhalt, diesel = False):
    if diesel == True:
        inhalt[0] += menge
        return True
    else:
        return False

tankinhalt  = [25.5]
tankvolumen =  30.0


tankenMitListe(tankvolumen, tankinhalt)
print("der Tankinhalt ist jetzt ", tankinhalt[0])

tankenMitListe(tankvolumen, tankinhalt, True)
print("der Tankinhalt ist jetzt ", tankinhalt[0])

# Fibonacci-Funktion mit Liste
# Listen, Operatoren
# append()
# del()
# remove()
# sort()
# insert(pos, wert)
# count()
# len()

def fibonacci(anzahlZahlen, listeFibonaccizahlen, ausdrucken= False):
    #Anzahl der Zahlen ermitteln
    #ist die Anzahl der Zahlen bereits in der Liste enthalten
    #neue Zahl erzeugen
    #neue Zahl anhängen (append)
    #solange, bis die anzahlZahlen erreicht ist
    while len(listeFibonaccizahlen) < anzahlZahlen:
        neueFibonaccizahl = listeFibonaccizahlen[-1] + listeFibonaccizahlen[-2]
        listeFibonaccizahlen.append(neueFibonaccizahl)

    if ausdrucken:
        print(listeFibonaccizahlen)

fibonacciZahlen = [1,1]
erzeugteZahlen  = 500

fibonacci(erzeugteZahlen, fibonacciZahlen, True)
      
erzeugteZahlen  = 600
fibonacci(erzeugteZahlen, fibonacciZahlen, True)

#erzeuge eine Funktion,die ähnlich wie oben eine Liste von Primzahlen erzeugt


