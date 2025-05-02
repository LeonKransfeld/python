def matheaufgaben():
    while True:
        op = input("Wähle eine Operation (+, -, *, /): ")
        try:
            zahl1 = float(input("Erste Zahl: "))
            zahl2 = float(input("Zweite Zahl: "))
            if op == '+':
                print(f"Ergebnis: {zahl1 + zahl2}")
            elif op == '-':
                print(f"Ergebnis: {zahl1 - zahl2}")
            elif op == '*':
                print(f"Ergebnis: {zahl1 * zahl2}")
            elif op == '/':
                print(f"Ergebnis: {zahl1 / zahl2}")
            else:
                print("Ungültige Operation")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")

matheaufgaben()