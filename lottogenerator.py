#Ziehung der Lottozahlen: 6 aus 49

#erstelle eine Funktion, welche eine sortierte Liste einer Ziehung wiedergibt. Verwende Zufallszahlen

import random

def lottoZiehung() :

    random.seed()
    lottozahlen = set() #keine doppelten Werte

    anzahlZahlenInZiehung = 6
                                    
    while anzahlZahlenInZiehung > len(lottozahlen):
        #eine Zahl "ziehen"
        eineZahl = random.randint(1, 49)
        #diese Zahl in das Set einfügen
        lottozahlen.add(eineZahl)
    

#anstatt:
#    lottozahlenList =  sorted(lottozahlen)
#    return lottozahlenList

    return sorted(lottozahlen)

#print( lottogenerator() )
