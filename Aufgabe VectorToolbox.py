# Aufgabe:
#
# erstelle eine vectorToolbox, welche
#
# VektorAddition
# Vektorbetrag
#
# als Funktionen enthält
#
# es sollen Vektoren beliebiger Dimension bearbeitet werden können


#anschließend sollen die beiden Vektoren (3, 0, -5) und (1, 4, 9) addiert werden

import vectorToolbox


vector1 = [3, 0, -5]
vector2 = [1, 4,  9]

result = vectorToolbox.add(vector1, vector2)
print(result)
