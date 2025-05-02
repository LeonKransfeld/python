class Fabrik:
    def __init__(self, anzahl:int, adresse:str):
        self.__adresse:str = adresse
        self.__anzahl:int = anzahl

    def setAdresse(self, adresse):
        self.__adresse = adresse

    def getAdresse(self) -> str:
        return self.__adresse

    def init_starteFabrik(self):

        

    def starteFabrik(self) -> None:
        for i in range(0, self.__anzahl, 1):
            print(f"Maschine {i+1} wurde gestartet...")



kleineFabrik = Fabrik(15, "Am Berg oben, 4 - 75635 Ort")
kleineFabrik.starteFabrik()
