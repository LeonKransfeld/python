#Zufallszahlen - Pseudozufallszahlen
import random

#Anfangspunkt der Zufallszahlen festlegen
random.seed()


a = random.randint(10,100)

b = random.randint(10,100)

#erweitern um die Grundrechenarten  * -

operatorenListe = ['+', '*', '-']
operation = random.randint(0,2)

# stellt + - oder * dar
# operatorenListe[operation]

exec(f"ergebnis = {a} {operatorenListe[operation]} {b}")

#ergebnis = a + b
#ergebnis = a * b
#ergebnis = a - b

print(f"Die Aufgabe: {a} {operatorenListe[operation]} {b}")

print("Bitte Lösungsvorschlag eingeben:")

#typecasting= erwingen es datentypen, hier: integer
benutzereingabe = int(  input()   )

if benutzereingabe == ergebnis:
    print(benutzereingabe, "ist richtig")
    
elif benutzereingabe < 0 or benutzereingabe > 100:
    print(benutzereingabe, "ist weit daneben")
    
elif ergebnis-1 <= benutzereingabe <= ergebnis+1:
    print(benutzereingabe, "ist nahe dran")
    
else:
    print(benutzereingabe, "ist falsch")
    
print("Ergebnis:", ergebnis)
