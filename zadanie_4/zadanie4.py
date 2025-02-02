import math
try:
    from multipledispatch import dispatch
except ImportError:
    print("Error: multipledispatch module not found. Install it using 'pip install multipledispatch'")

class Figura:
    """Klasa bazowa dla wszystkich figur."""
    def opis(self):
        """Zwraca opis figury."""
        return "Figura bazowa"

class Prostokat(Figura):
    """Klasa reprezentująca prostokąt."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def opis(self):
        """Zwraca opis prostokąta."""
        return f"Prostokąt o wymiarach {self.x}x{self.y}"

    def pole(self):
        return self.x * self.y

class Kwadrat(Prostokat):
    """Klasa reprezentująca kwadrat."""
    def __init__(self, x: int):
        super().__init__(x, x)

    def opis(self):
        """Zwraca opis kwadratu."""
        return f"Kwadrat o boku {self.x}"

class Kolo(Figura):
    """Klasa reprezentująca koło."""
    def __init__(self, r: float):
        self.r = r

    def opis(self):
        """Zwraca opis koła."""
        return f"Koło o promieniu {self.r}"

    def pole(self):
        return math.pi * self.r ** 2

def pola_powierzchni(lista_figur):
    """Wyświetla pola powierzchni dla listy figur."""
    for figura in lista_figur:
        if hasattr(figura, 'pole'):
            print(f"Pole obiektu: {figura.pole()}")
        else:
            print(f"Brak pola dla obiektu: {figura.opis()}")

if __name__ == "__main__":
    a = Figura()
    b = Prostokat(2, 4)
    c = Kwadrat(2)
    d = Kolo(3)

    print(f"Pole prostokąta (2x4): {b.pole()}")
    print(f"Pole kwadratu (bok=2): {c.pole()}")
    print(f"Pole koła (r=3): {d.pole()}")

    pola_powierzchni([a, b, c, d])