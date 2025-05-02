from abc import ABC, abstractmethod
class Mensch(ABC):
    def __init__(self, Name):
        self._Name=Name

        @abstractmethod
        def lesen(self):
            pass

class Kind(Mensch):
    def __init__(self, Name):
        super().__init__(Name)

    def lesen(self):
        print("Kind liest Name langsam: ", self._Name)

class Erwachsener(Mensch):
    def __init__(self, Name):
        super().__init__(Name)

    def lesen(self):
        print(f"Erwachsener liest Name ", self._Name)

irgendeinMensch : Mensch

irgendeinMensch=Kind("Hans")
irgendeinMensch.lesen()

irgendeinMensch=Erwachsener("Peter")
irgendeinMensch.lesen()