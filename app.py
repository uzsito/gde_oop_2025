from jar import BelfJarat, NemzJarat
from ltars import LTars
from fogl import Fogl

def main():
    lt = LTars("Mystra Airlines")

    j1 = BelfJarat("B123", "Baldur's Gate", 18000)
    j2 = NemzJarat("N456", "Moonrise Towers", 75000)
    j3 = NemzJarat("N789", "Elturel", 135000)

    lt.add_jarat(j1)
    lt.add_jarat(j2)
    lt.add_jarat(j3)

    fogl_lista = [
        Fogl("Tav", j1),
        Fogl("Shadowheart", j2),
        Fogl("Astarion", j3),
        Fogl("Lae'zel", j1),
        Fogl("Wyll", j2),
        Fogl("Karlach", j3)
    ]

    while True:
        print("+-------------------------------------------+")
        print("|    REPÜLŐJEGY FOGLALÓ - MYSTRA AIRLINES   |")
        print("+-------------------------------------------+")
        print("|          1  Új foglalás                   |")
        print("|          2  Foglalás törlése              |")
        print("|          3  Foglalások megnézése          |")
        print("|          4  Kilépés                       |")
        print("+-------------------------------------------+")

        valasztas = input("Válassz egy lehetőséget (1-4): ")

        if valasztas == "1":
            utas = input("Add meg az utas nevét: ")
            print("\nElérhető járatok:")
            for idx, jarat in enumerate(lt.list_jaratok(), 1):
                print(f" {idx}. {jarat}")
            try:
                kiv_idx = int(input("\nVálasztott járat sorszáma: ")) - 1
                kivalasztott = lt.jaratok[kiv_idx]
                ujfogl = Fogl(utas, kivalasztott)
                fogl_lista.append(ujfogl)
                print(f"\n>>> Sikeres foglalás: {kivalasztott.ar} Ft")
            except (IndexError, ValueError):
                print("\n!!! Hibás választás!")

        elif valasztas == "2":
            utas = input("Add meg a törlendő foglalás nevét: ")
            torolve = False
            for fogl in fogl_lista:
                if fogl.utas == utas:
                    fogl_lista.remove(fogl)
                    print("\n>>> Foglalás törölve.")
                    torolve = True
                    break
            if not torolve:
                print("\n!!! Nincs ilyen nevű foglalás.")

        elif valasztas == "3":
            if not fogl_lista:
                print("\n>>> Nincsenek aktív foglalások.")
            else:
                print("\n>>> Aktív foglalások:")
                for fogl in fogl_lista:
                    print(fogl.fogl_info())

        elif valasztas == "4":
            print("\nKilépés... Köszönjük a használatot!")
            break
        else:
            print("\n!!! Hibás választás!")

if __name__ == "__main__":
    main()
