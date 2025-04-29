import sys
import mysql.connector

import tkinter # toolkit interface

#try-catch-Block
#..dient dazu, schwere Fehler abzufangn und darauf zu reagieren

try:
    verbindung = mysql.connector.connect(host = "localhost", user ="root", passwd="")

except:
    print("Keine Verbindung zum Server") 
    sys.exit(0)

cursor = verbindung.cursor()

cursor.execute("SHOW DATABASES")

for datenbank in cursor:
    print(datenbank)

#-------ab hier GUI---------------------------------------------
# snake_case kann verwendet werden
# UpperCamelCase (PascalCase): Klassenbezeichner
# lowerCamelCase: Variablen, Funktionen etc



def ende():
    mainWindow.destroy()

def ausgabe():
    labelAuswahl["text"] = datenbankListe.get("active")

    
mainWindow = tkinter.Tk()
mainWindow.title("Datenbankauswahl")
labelAuswahl = tkinter.Label(mainWindow, text="Gewählte Datenbank:")
labelAuswahl.pack()

datenbankListe = tkinter.Listbox(mainWindow, height = 0)

# 1. Versuch
#datenbankListe.insert("end", "PSE")
#datenbankListe.insert("end", "HOYT")
#datenbankListe.pack()

cursor.execute("SHOW DATABASES")

for datenbank in cursor:
    datenbankListe.insert("end", datenbank)

datenbankListe.pack()

mainWindow.mainloop()

