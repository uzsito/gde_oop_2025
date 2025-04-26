from jar import Jarat

class LTars:
    def __init__(self, nev: str):
        self.nev = nev
        self.jaratok = []

    def add_jarat(self, jarat: Jarat):
        self.jaratok.append(jarat)

    def list_jaratok(self):
        return [jarat.info() for jarat in self.jaratok]
