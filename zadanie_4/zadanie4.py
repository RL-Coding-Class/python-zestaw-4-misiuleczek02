import math
from multipledispatch import dispatch

class Figura:
    """Klasa bazowa dla wszystkich figur."""
    def __init__(self):
        pass

class Prostokat(Figura):
    """Klasa reprezentująca prostokąt."""
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    """Klasa reprezentująca kwadrat (szczególny przypadek prostokąta)."""
    def __init__(self, x: int):
        super().__init__(x, x)

class Kolo(Figura):
    """Klasa reprezentująca koło."""
    def __init__(self, r: float):
        super().__init__()
        self.r = r

@dispatch(Figura)
def pole(instance: Figura):
    """Zwraca pole dla klasy Figura."""
    return 0

@dispatch(Prostokat)
def pole(instance: Prostokat):
    """Zwraca pole prostokąta."""
    return instance.x * instance.y

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x: int, y: int):
    """Zwraca pole prostokąta po zmianie jego wymiarów."""
    instance.x = x
    instance.y = y
    return x * y

@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    """Zwraca pole kwadratu."""
    return instance.x ** 2

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x: int):
    """Zwraca pole kwadratu po zmianie jego boku."""
    instance.x = x
    instance.y = x
    return x ** 2

@dispatch(Kolo)
def pole(instance: Kolo):
    """Zwraca pole koła."""
    return math.pi * instance.r ** 2

@dispatch(Kolo, float)
def pole(instance: Kolo, r: float):
    """Zwraca pole koła po zmianie jego promienia."""
    instance.r = r
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
