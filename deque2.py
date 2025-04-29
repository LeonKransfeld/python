import collections
d = collections.deque([8, 18, 28])

print("Erstellt:", d)

d.appendleft([5, 55])
print("Element angefügt:", d)

d.append([25, "Willy-Brand-Platz"])
print("Element angefügt:", d)

d.insert(2, 11)
print("Element eingefügt:", d)

d.extendleft([7,9])
print("Elemente angefügt:", d)

d.extend([17,19])
print("Elemente angefügt:", d)

x = 5
if x in d:
    print(f"Position von {x}: {d.index(5)}")

#Versuch: nicht vorhandenes Element indizieren
#x = 13
#print(f"Position von {x}: {d.index(x)}")
# Erzeugt einen ValueError

dCopy = d.copy()
    
for i in range(5):
    li = d.popleft()
    print("Entferntes Element, links:", li)
    re = d.pop()
    print("Entferntes Element, rechts:", re)
    
print("Danach:", d)

print("dCopy: ", dCopy)

dCopy.rotate(5) 
print("Nach Rotation um +5:", dCopy)

dCopy.rotate(-3)
print("Nach Rotation um -3:", dCopy)

#Aufgabe: Getränkeautomat
#einfachste Version: nur ein Getränk mit einem Preis
#Der Kunde gibt in der Regel kein Passendes Geld ein, sondern braucht Rückgeld
#Der Getränkeautomat hat einzelne Zähler für die Münzarten 5 Cent, 10 Cent, 20 Cent,...
#Der Kunde wird entweder aufgefordert passend einzugeben oder ihm wird passendes Wechselgeld ausgegeben




