import math
from multipledispatch import dispatch

class Figura:
    """Klasa bazowa dla wszystkich figur."""
    def __init__(self):
        pass

    def opis(self):
        """Zwraca opis figury."""
        return "Figura bazowa"

class Prostokat(Figura):
    """Klasa reprezentująca prostokąt."""
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

    def opis(self):
        """Zwraca opis prostokąta."""
        return f"Prostokąt o wymiarach {self.x}x{self.y}"

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

@dispatch(Figura)
def pole(instance):
    """Zwraca pole dla klasy Figura."""
    return 0

@dispatch(Prostokat)
def pole(instance):
    """Zwraca pole prostokąta."""
    return instance.x * instance.y

@dispatch(Prostokat, int, int)
def pole(instance, x, y):
    """Zmienia wymiary prostokąta i zwraca jego pole."""
    instance.x = x
    instance.y = y
    return x * y

@dispatch(Kwadrat)
def pole(instance):
    """Zwraca pole kwadratu."""
    return instance.x ** 2

@dispatch(Kwadrat, int)
def pole(instance, x):
    """Zmienia bok kwadratu i zwraca jego pole."""
    instance.x = x
    instance.y = x
    return x ** 2

@dispatch(Kolo)
def pole(instance):
    """Zwraca pole koła."""
    return math.pi * instance.r ** 2

@dispatch(Kolo, float)
def pole(instance, r):
    """Zmienia promień koła i zwraca jego pole."""
    instance.r = r
    return math.pi * r ** 2

def polaPowierzchni(lista_figur):
    """Wyświetla pola powierzchni dla listy figur."""
    for figura in lista_figur:
        print(f"Pole obiektu: {pole(figura)}")

if __name__ == "__main__":
    a = Figura()
    b = Prostokat(2, 4)
    c = Kwadrat(2)
    d = Kolo(3)

    print(f"Pole prostokąta (2x4): {pole(b)}")
    print(f"Pole kwadratu (bok=2): {pole(c)}")
    print(f"Pole koła (r=3): {pole(d)}")

    print(f"Pole prostokąta po zmianie na 5x6: {pole(b, 5, 6)}")
    print(f"Pole kwadratu po zmianie boku na 7: {pole(c, 7)}")
    print(f"Pole koła po zmianie promienia na 4.0: {pole(d, 4.0)}")

    polaPowierzchni([a, b, c, d])

