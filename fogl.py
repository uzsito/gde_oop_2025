from jar import Jarat

class Fogl:
    def __init__(self, utas: str, jarat: Jarat):
        self.utas = utas
        self.jarat = jarat

    def fogl_info(self) -> str:
        return f"Utas: {self.utas}, {self.jarat.info()}"
