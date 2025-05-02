import random

def slot_maschine():
    # Symbole für die Slot-Maschine
    symbole = ['🍒', '🍋', '🍉', '🔔', '⭐', '💎']

    while True:
        # Eingabe, um das Spiel zu starten oder zu beenden
        eingabe = input("Drücke 'Enter', um zu spielen oder 'q', um zu beenden: ")
        if eingabe.lower() == 'q':
            print("Spiel beendet.")
            break

        # Erzeuge ein 3x3 Raster mit zufälligen Symbolen
        raster = [[random.choice(symbole) for _ in range(3)] for _ in range(3)]

        # Ausgabe des Rasters
        print("\n--- Slot Maschine ---")
        for zeile in raster:
            print(' | '.join(zeile))
        print("---------------------\n")

        # Beispielauswertung (einfach)
        if any(zeile[0] == zeile[1] == zeile[2] for zeile in raster):
            print("Glückwunsch! Du hast eine Reihe getroffen!\n")
        else:
            print("Leider keine Gewinnreihe. Viel Glück beim nächsten Mal!\n")

slot_maschine()