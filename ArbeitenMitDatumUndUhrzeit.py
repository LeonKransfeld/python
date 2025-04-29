# Arbeiten mit Datum und Uhrzeit


import time as libTime

#UNIX-Timestamp mit libTime()
print("libTime():", libTime.time())

tag          = 2
monat        = 1 
jahr         = 0
stunde       = 3 
minute       = 4 
sekunde      = 5
wochentag    = 6
tagDesJahres = 7
sommerzeit   = 8

#für jetzigen Augenblick
lokaleZeit = libTime.localtime()
print("localtime():", f"{lokaleZeit[tag]:02d}.{lokaleZeit[monat]:02d}.{lokaleZeit[jahr]} "
                      f"{lokaleZeit[stunde]:02d}:{lokaleZeit[minute]:02d}:{lokaleZeit[sekunde]:02d}")

# ???? Zeile 14 ??? -> zur besseren Lesbarkeit
sekunden   = 3_850_000_000
lokaleZeit = libTime.localtime(sekunden)

print("localtime():", f"{lokaleZeit[tag]:02d}.{lokaleZeit[monat]:02d}.{lokaleZeit[jahr]} "
                      f"{lokaleZeit[stunde]:02d}:{lokaleZeit[minute]:02d}:{lokaleZeit[sekunde]:02d}")

#??? was ist das???
tu = 2022, 1, 15, 12, 35, 20, 0, 0, 0
print("tu ist vom Datentyp ", type(tu) )

                            #string-format-libTime
print("strftime():", libTime.strftime("%d.%m.%Y %H:%M:%S"))
print("strftime():", libTime.strftime("%d.%m.%y %H:%M:%S"))
print("strftime():", libTime.strftime("%d.%m.%Y %H:%M:%S", tu))
print("strftime():", libTime.strftime("%d.%m.%Y %H:%M:%S", lokaleZeit))

print("mktime():", libTime.mktime(tu))
print("mktime():", libTime.mktime(lokaleZeit))

#--------------------------------------------------------------------

z_start = 2022, 2, 15, 22, 45, 0, 0, 0, 0
print("Start:", libTime.strftime("%d.%m.%Y %H:%M:%S", z_start))
mk_start = libTime.mktime(z_start)

z_ende  = 2022, 2, 15, 22, 55, 15, 0, 0, 0
print("Ende: ", libTime.strftime("%d.%m.%Y %H:%M:%S", z_ende))
mk_ende = libTime.mktime(z_ende)

print()
print("Differenz:")
diff_sek = mk_ende - mk_start
diff_min = diff_sek/60
diff_std = diff_min/60
diff_tag = diff_std/24
print(diff_sek, "Sekunden")
print(diff_min, "Minuten")
print(diff_std, "Stunden")
print(diff_tag, "Tage")

#00:10:15 als Ausgabe!
vergangeneZeit   = mk_ende - mk_start
ltVergangeneZeit = libTime.localtime(vergangeneZeit)
print(f"{ltVergangeneZeit[stunde]}:{ltVergangeneZeit[minute]}:{ltVergangeneZeit[sekunde]}")
print(ltVergangeneZeit)
# Warum wird als Differenzstunde 1 ausgegeben?

#schreibe eine Funktion "tageBisZUm Geburtstag(geburtsdatum:Liste):integer


