from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, kod: str, cel: str, ar: int):
        self.kod = kod
        self.cel = cel
        self.ar = ar

    @abstractmethod
    def info(self) -> str:
        pass

class BelfJarat(Jarat):
    def info(self) -> str:
        return f"Belföldi Járat - Kód: {self.kod}, Cél: {self.cel}, Ár: {self.ar} Ft"

class NemzJarat(Jarat):
    def info(self) -> str:
        return f"Nemzetközi Járat - Kód: {self.kod}, Cél: {self.cel}, Ár: {self.ar} Ft"
