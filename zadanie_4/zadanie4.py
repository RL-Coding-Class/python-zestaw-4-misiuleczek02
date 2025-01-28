import math
from multipledispatch import dispatch

class Figura:
    """Klasa bazowa dla wszystkich figur."""
    def __init__(self):
        pass

    def opis(self):
        """Zwraca opis figury."""
        return "Figura bazowa"

    def parametry(self):
        """Zwraca parametry figury."""
        return {}

class Prostokat(Figura):
    """Klasa reprezentująca prostokąt."""
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

    def opis(self):
        """Zwraca opis prostokąta."""
        return f"Prostokąt o wymiarach {self.x}x{self.y}"

    def parametry(self):
        """Zwraca parametry prostokąta."""
        return {"x": self.x, "y": self.y}

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
        super().__init__()
        self.r = r

    def opis(self):
        """Zwraca opis koła."""
        return f"Koło o promieniu {self.r}"

    def parametry(self):
        """Zwraca parametry koła."""
        return {"r": self.r}

@dispatch(Figura)
def pole(figura):
    """Zwraca pole dla klasy Figura."""
    return 0

@dispatch(Prostokat)
def pole(prostokat):
    """Zwraca pole prostokąta."""
    return prostokat.x * prostokat.y

@dispatch(Prostokat, int, int)
def pole(prostokat, x, y):
    """Zwraca pole prostokąta po zmianie jego wymiarów."""
    prostokat.x = x
    prostokat.y = y
    return x * y

@dispatch(Kwadrat)
def pole(kwadrat):
    """Zwraca pole kwadratu."""
    return kwadrat.x ** 2

@dispatch(Kwadrat, int)
def pole(kwadrat, x):
    """Zwraca pole kwadratu po zmianie jego boku."""
    kwadrat.x = x
    kwadrat.y = x
    return x ** 2

@dispatch(Kolo)
def pole(kolo):
    """Zwraca pole koła."""
    return math.pi * kolo.r ** 2

@dispatch(Kolo, float)
def pole(kolo, r):
    """Zwraca pole koła po zmianie jego promienia."""
    kolo.r = r
    return math.pi * r ** 2

def pola_powierzchni(lista_figur):
    """Wyświetla pola powierzchni dla listy figur."""
    for figura in lista_figur:
        print(f"Pole obiektu: {pole(figura)}")

if __name__ == "__main__":
    a, b, c, d = Figura(), Prostokat(2, 4), Kwadrat(2), Kolo(3)

    print(f"Pole prostokąta (2x4): {pole(b)}")
    print(f"Pole kwadratu (bok=2): {pole(c)}")
    print(f"Pole koła (r=3): {pole(d)}")

    print(f"Pole prostokąta po zmianie na 5x6: {pole(b, 5, 6)}")
    print(f"Pole kwadratu po zmianie boku na 7: {pole(c, 7)}")
    print(f"Pole koła po zmianie promienia na 4: {pole(d, 4.0)}")

    pola_powierzchni([a, b, c, d])
