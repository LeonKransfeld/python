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

#fehlende Datenbank erzeugen, falls nicht vorhanden
cursor.execute("CREATE DATABASE IF NOT EXISTS 2024SommerFIAEA2Python")

cursor.execute("SHOW DATABASES")

for datenbank in cursor:
    print(datenbank)

#-------ab hier GUI---------------------------------------------
# snake_case kann verwendet werden
# UpperCamelCase (PascalCase): Klassenbezeichner
# lowerCamelCase: Variablen, Funktionen etc



def ende():
    mainWindow.destroy()

def auswahlAusgeben():
    lbAuswahl["text"] = liDatenbank.get("active")

def datenbankFensterErzeugen(datenbankname):
    wDatenbank = tkinter.Tk()           # neues Fenstererzeugen
    wDatenbank.title(datenbankname)     # Titel des Fensters
    wDatenbank.resizable(True, True)    # Breite und Höhe veränderbar
    mainWindow.destroy()                # Hauptfenster schließen
     

#leere Funktion mit pass definieren, Übergangslösung
def nurGeplantNIchtImplementiert():
    pass
    
    
mainWindow = tkinter.Tk()
mainWindow.title("Datenbankauswahl")

#Widget: Label = Beschriftung
lbAuswahl = tkinter.Label(mainWindow, text="Gewählte Datenbank:")
lbAuswahl.grid(row=0, column=0, padx=5, pady=5)

#Widget: Frame= Rahmen
frRahmen = tkinter.Frame(mainWindow)
frRahmen.grid(row=1, column=0, padx=5, pady=5) 

#anstatt der Listbox wird jetzt eine Scrollbar verwendet
#datenbankListe = tkinter.Listbox(mainWindow, height = 0)
sbDatenbankListe = tkinter.Scrollbar(frRahmen, orient="vertical")

# nächster Schritt: die Scrollbar mit Werten versehen...
liDatenbank = tkinter.Listbox(frRahmen, height=5, yscrollcommand=sbDatenbankListe.set)
sbDatenbankListe["command"] = liDatenbank.yview

cursor.execute("SHOW DATABASES")
for datenbank in cursor:
    liDatenbank.insert("end", datenbank)

liDatenbank.grid(row=0, column=0)
sbDatenbankListe.grid(row=0, column=1, sticky="sn") #von oben nach unten

buAuswahl = tkinter.Button(mainWindow, text="Auswählen", command=auswahlAusgeben, width=10)
buAuswahl.grid(row=2, column=0, sticky="w", padx=5, pady=5)

mainWindow.mainloop()

