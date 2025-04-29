# einen Tipp in Form einer Liste definieren
# Lottozahlen ziehen
# den Tipp auswerten

      #Dateiname
import lottogenerator

#Test: importieren der eigenen Funktion
print(lottogenerator.lottoZiehung()  )

meinTipp = [2, 7, 15, 33, 35, 42]
ziehung  = lottogenerator.lottoZiehung()

anzahlRichtigeZahlen = 0

for meineZahl in meinTipp:
    for gezogeneZahl in ziehung:
        if gezogeneZahl== meineZahl:
            anzahlRichtigeZahlen += 1

print(ziehung, meinTipp,"Anzahl Richtige: ", anzahlRichtigeZahlen)

#Aufgabe: schreibe diesen Algorithmus als Funktion
