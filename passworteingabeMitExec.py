import tkinter

def ende():
    wEingabedialog.destroy()

def pruefen():
    #lesen des Eingabefeldes
    pw = etPasswort.get()
    
    if pw == "Bingo":
        lbErgebnis["text"] = "Eingabe richtig"
    else:
        lbErgebnis["text"] = "Eingabe falsch"

    #Eingabefeld löschen: ab Position 0 bis zum Ende (also vollständig)    
    etPasswort.delete(0, "end")

    buBeenden["state"] = "normal"

                     #window+Gadget
def imGridPlatzieren(widget, rowNr, colNr, paddingX, paddingY, stickIt = ""):
    #exec und eval
    exec("widget.grid( row="      + f"{rowNr}"
                  + ", column="   + f"{colNr}"
                  + ", padx="     + f"{paddingX}"
                  + ", pady="     + f"{paddingY}"
                  + ", sticky=\"" + stickIt + "\")")
    # escapen: die Funktion des Zeichens " deaktivieren durch den \
#Aufruf: imGridPlatzieren(lbPasswort, 0, 0, 5 ,5, "w")

#lbPasswort.grid(       row=0, column=0, sticky="w", padx=5, pady=5)
#etPasswort.grid(       row=1, column=0,             padx=5, pady=5)
#buPasswortPruefen.grid(row=2, column=0, sticky="w", padx=5, pady=5)


wEingabedialog = tkinter.Tk()
wEingabedialog.title("Passworteingabe")
wEingabedialog.resizable(False, False)

lbPasswort = tkinter.Label(wEingabedialog, text="Passwort eingeben:")
#lbPasswort.grid(row=0, column=0, sticky="w", padx=5, pady=5)
imGridPlatzieren(lbPasswort, 0, 0, 5, 5, "w")

#verdeckte Eingabe durch show="*"
etPasswort = tkinter.Entry(wEingabedialog, show="*")
etPasswort.grid(row=1, column=0, padx=5, pady=5)

buPasswortPruefen = tkinter.Button(wEingabedialog, text="Passwort prüfen",
                                   command=pruefen, width=12)
buPasswortPruefen.grid(row=2, column=0, sticky="w", padx=5, pady=5)

lbErgebnis = tkinter.Label(wEingabedialog, text="(nicht geprüft)")
lbErgebnis.grid(row=3, column=0, sticky="w", padx=5, pady=5)

buBeenden = tkinter.Button(wEingabedialog, text="Beenden", command=ende,
                           width=10, state="disabled")
buBeenden.grid(row=4, column=1,  padx=5, pady=5)

wEingabedialog.mainloop()
