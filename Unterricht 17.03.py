from abc import ABC, abstractmethod


class Besucher(ABC):
    def createBesucher(typ: str):  # static-Methode in Python
        match (typ):
            case "STANDARD":
                return ...
            case "PREMIUM":
                return ...
            case "VIP":
                return ...

    @abstractmethod
    def isExpressEingang(self, isWerktag: bool = True) -> bool:
        pass

    @abstractmethod
    def calculatePreis(self, basisPreis: float = 0.0) -> float:
        pass


class Standard(Besucher):
    def isExpressEingang(self, isWerktag: bool = False) -> bool:
        print("Standard-Besucher: isExpressEingang")
        return False

    def calculatePreis(self, basisPreis: float = 0.0) -> float:
        print("Standard-Besucher: calculatePreis")
        return basisPreis


class Premium(Besucher):
    def isExpressEingang(self, isWerktag: bool) -> bool:
        print("Premium-Besucher: isExpressEingang")
        return isWerktag

    def calculatePreis(self, basisPreis: float = 0.0) -> float:
        print("Premium-Besucher: calculatePreis")
        return basisPreis * 0.95


class Vip(Besucher):
    def isExpressEingang(self, isWerktag: bool) -> bool:
        print("VIP-Besucher: isExpressEingang")
        return True

    def calculatePreis(self, basisPreis: float = 0.0) -> float:
        print("VIP-Besucher: calculatePreis")
        return basisPreis * 0.90


einBesucher = Besucher("STANDARD")
print(einBesucher.isExpressEingang())