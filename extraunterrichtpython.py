# Variablen und Operatoren
# Variable dienen als Speicherorte für Werte. In Python muss der Datentype einer Variable nicht explizit angegeben werden.
zahl=10
name="Python"
pi=3.14
 
# Arten von Operatoren
# 1. Arithmetische Operatoren
 
# + Addition
# - Subtraktion
# * Multiplikation
# / Division
# ** Potenzierung
# // Ganzzahldivision
# % Modulo (Rest bei Division)
 
# a,b= 7,3
a=7
b=3
print (a+b)
print(a**b)
 
# 2. Vergleichsoperatoren
# Überprufen, ob zwei Werte gleich, ungleich oder in einer bestimmten Beziehung zueinander stehen.
 
# == (gleich): Prüft, ob zwei Werte gleich sind.
# != (ungleich): Prüft, ob zwei Werte ungleich sind.
# >  (größe als): Prüft, ob der linke Wert größer als der rechte ist.
# <  (kleiner als): Prüft, ob der linke Wert kleiner als der rechte ist.
# >= (größer oder gleich): Prüft, ob der linke Wert größer oder gleich dem rechten Wert ist.
# <= (kleiner oder gleich): Prüft, ob der linke Wert kleiner oder gleich dem rechten Wert ist.
 
a,b,c,d,e,f,g= 6,3,5,6,8,10,3
 
 
# 3. Logische Operatoren
# Logische Operatoren werden verwendet, um boolesche Ausdrücke zu kombinieren und bedingungen zu prüfen.
 
# and : Gibt True zurück, wenn beide Bedingungen wahr sind, anderenfall False.
# or  : Gibt True zurück, wenn mindestens eine Bedingung wahr ist
# not : kehrt den Wahrheitswert einer Bedingung um. Wenn die Bedingung True ist, wird zu False und umgekehrt.
 
# 4. Datentypen
# 4.1. Zahlentype
 
# Integer (int)- Ganze Zahlen
# Der int-Type repräsentiert ganze Zahlen, d.h., Zahlen ohne Dezimalstellen.
 
a,b,c= 5, -3, 0
 
# floatnumber (float)- Fließkommazahlen
# Der float-Type repräsentiert Zahlen mit Dezimalstellen oder auch Zahlen in wissenschaftlicher Notation.
a,b,c= 3.14, -0.02, 2.5e5
 
# Komplexe Zahlen (complex)- Zahlen mit realem und imaginärem Teil
# Der complex-Type wird verwendet, um komplexe zahlen zu repräsentieren, die einen realen und einen imaginären Teil haben.
a,b = 2+3j ,1-4j
 
 
# 4.2. Text (string Type)
# str (string)
# Der Str-Type steht für Zeichenketten (Strings). Ein String ist eine Folge von Zeichen, die in einfache (') oder doppelte ("")
# Anführungszeichen eingeschlossen werden.
 "Python"
"4"
 
# In Python können wir zwieschen verschiedenen datentypen unwandeln.
#  
 
# 4.3. Boolean (bool)- Wahrheitswerte
# Der bool- Datentype hat nur zwei Werte: True und False.
# verwendung: wird in bedingten Ausdrücken, Vergleichen und logischen Operationen verwendet.
Treu, False
 
# 4.4. Sammlungen ( collection Types)
 
# list (Liste):
# Eine geordnete Sammlung von Werten, die veränderlich ist und beliebige Datentypen enthalten kann.
liste1=[1, "Python", 3.14, True ]
# Verwendung: wird verwendet, um eine Sammlung von Elementen zu Speichern, auf die durch Indizes zugegriffen werden kann.
# Zugriffsoperator (Mit dem Indexoperator)
# Hinzufügen von Elementen zu einer Liste ( .append() , .insert())
# Entfern von Elementen aus einer Liste ( list.remove(element), list.pop(index), list.clear(), del liste[start_index:end_index])
# Konkatenation( + )
# Wiederholung (*)
# in-Operator
# index-suche ( liste.index(element))
 
# tuple (Tupel):
# ein geordnete Sammlung von Werten, die unveränderlich ist.
tuple1=(1,2,4,"Python")
# Verwendung: wird verwendet, wenn eine unveränderliche Sammlung von Werten erforderlich ist.
# Zugriffsoperator (Mit dem Indexoperator)
# Konkatenation( + )
# Wiederholung (*)
# index-suche ( liste.index(element))
 
# set (Menge):
# Eine ungeordnete Sammlung von einzigartigen Werten (Keine Duplikate)
menge1= {1,2,3,4}
# Verwendung: wird verwendet, um Mengen ohne Duplikate zu speichern.
# Vereinigung (set1|set2) oder set1.union(set2)
# Schnittmenge (&) oder .intersection()
# Differenz (-) oder set1.differenz(set2) =?set2.differenz(set1)
# Symmetrische Differenz (^) oder .Symetric_difference()
# subset (<=) oder .issubset()
# obermenge (>=) oder . issuperset()
# disjunk (.isdisjoint())
 
# dict (Wörterbuch):
# Eine Sammlung von Schlüssel-Wert-Paaren, die unveränderlich ist.
dict1= {"name": Sara, "age": 26}
#Verwendung: wird verwendet, um Daten mit einer Zuordnung von Schlüsseln zu Werten zu speichern.
# zugriffen auf Werte über Schlüssel (wert=dict[Schlüssel])
# in- Operator (schlüssel in dict)
# del dict[schlüssel]
# # vergleichen == , !=
# update () ( dict.update(anderes_dict))
# dict.items()
# dict.keys()
# dict.values()

# dict (Wörterbuch):
# Eine Sammlung von Schlüssel-Wert-Paaren, die unveränderlich ist.
# Man erstellt ein Dictionary, indem man geschweifte Klammern {} benutzt und die Schlüssel-Wert-Paare hineinschreibt.
Syntax
name_dict={"Schlüssel1": "Wert1",
           "Schlüssel2": "Wert2"
}
dict1= {"name":Sara, "age": 26}
#Verwendung: wird verwendet, um Daten mit einer Zuordnung von Schlüsseln zu Werten zu speichern.
# Wichtige Eigenschaften: Veränderbar: Elemente können hinzufügt, geändert oder entfernt werden.
# Jeder Schlüssel im Dictionary muss eindeutig sein.
# zugriffen auf Werte über Schlüssel (wert=dict[Schlüssel])
# in- Operator (schlüssel in dict)
# del dict[schlüssel]
# # vergleichen == , !=
# update () ( dict.update(anderes_dict))
# dict.items()
# dict.keys()
# dict.values()
 
 
# Sonderdatentype
# None:
# Ein spezieller Datentype, der das Fehlen von Wert oder einen leeren Wert darstellt.
# Verwendung: wird verwendet, um eine leere oder nicht initialisierte Variable darzustellen.
 
# 5. Verzweigungen (Bedingungen prüfen und Entscheidung treffen) (if, elif, else)
# Verzweigung werden verwendet, um Bedingungen zu prüfen und verschiedene Codeblöcke auszuführen, je nachdem, ob die Bedingung erfüllt ist.
# Einfache if-else-Bedingung
 
Syntax:
if Bedingung:
  # Anweisungen, wenn bedingung wahr ist.
else:
  # Anweisungen, wenn die Bedingung falsch ist.
 
# Der ternäre Operator (Tarnary Operator) ist eine Kompakte Möglichkeit, eine einfache Bedingung zu Überprüfen
# und je nach ergebnis einen Wert zurückzugeben. Es wird auch bedingter Ausdruck genannt. Der ternär Operator ist eine Kurzform
# für eine if-else-Bedingung.
# Für einfach Bedingungen kann die if-else-Anweisung in einer einzigen Zeile geschrieben werden.
 
 
# Prüfung von mehreren Bedingungen (if-elif-else)
 
Syntax:
if Bedingung1:
   # Block wird ausgeführt, wenn Bedingung1 True ist
   Anweisung1
elif andere_Bedingung:
   # Block wird ausgeführt, wenn Bedingung1 False und andere_Bedingung True ist
   Anweisung
else:
   # Block wird ausgeführt, wenn keine Bedingung True ist
 
 
#Übung: Schreibe eine Programm, das den Eintrittspreis basierend auf dem Alter einer Person berechnet:
# personen unter 6 Jahren: Eintritt frei.
# Personen zwischen 6 und 17 Jahren: Kinderpreis : (5 Euro)
# Personen zwischen 18 und 64 Jahren: Standardpreis (10 Euro)
#Personen ab 65 Jahren: Seniorenrabatt (7 Euro)
 
 
# 6. Schleifen (Loops)
# Schleifen werden verwendet, um einen Codeblock wiederholt auszuführen.
 
# 6.1. for-schleife
# die for -schleife in Python wird verwendet, um über eine Sequenz (z.B Liste, Tupel, String, Dictionary oder range) zu iterieren.
Syntax:
for element in sequenz:
#   Codeblock, der für jedes Element der Sequenz ausgeführt wird.
 
# element : eine Variable, die bei jeder Iteration den aktuellen Wert aus der Sequenz annimmt.
# sequenz: Eine Sammlung von Elementen wie eine Liste, ein String, ein Dictionary oder eine range.
 
# Iterieren über eine Liste
# Iterieren über einen String
# verwenden von range
# Iterieren über ein Dictionary
# break und continue
# Verschachtelte Schleifen

#print("Pruduct\tpreis")
#print("Apfel\t1.20")
#print("orange\t0.9")