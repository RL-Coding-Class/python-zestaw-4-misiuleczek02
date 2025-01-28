from multipledispatch import dispatch
import math

# Klasa bazowa Figura
class Figura(object):
    def __init__(self):
        pass

# Klasa Prostokat
class Prostokat(Figura):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

# Klasa Kwadrat
class Kwadrat(Prostokat):
    def __init__(self, x: int):
        super().__init__(x, x)

# Klasa Kolo
class Kolo(Figura):
    def __init__(self, r: float):
        super().__init__()
        self.r = r

# Funkcja pole dla klasy Figura
@dispatch(Figura)
def pole(instance: Figura):
    return 0

# Funkcja pole dla klasy Prostokat (bez podania dodatkowych argumentów)
@dispatch(Prostokat)
def pole(instance: Prostokat):
    return instance.x * instance.y

# Funkcja pole dla klasy Prostokat (z podaniem boków jako argumentów)
@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x: int, y: int):
    instance.x = x
    instance.y = y
    return x * y

# Funkcja pole dla klasy Kwadrat (bez podania dodatkowych argumentów)
@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    return instance.x ** 2

# Funkcja pole dla klasy Kwadrat (z podaniem boku jako argumentu)
@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x: int):
    instance.x = x
    instance.y = x
    return x ** 2

# Funkcja pole dla klasy Kolo (bez podania dodatkowych argumentów)
@dispatch(Kolo)
def pole(instance: Kolo):
    return math.pi * instance.r ** 2

# Funkcja pole dla klasy Kolo (z podaniem promienia jako argumentu)
@dispatch(Kolo, float)
def pole(instance: Kolo, r: float):
    instance.r = r
    return math.pi * r ** 2

# Funkcja do wyliczania pola dla listy obiektów
def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(f"Pole obiektu: {pole(i)}")

if __name__ == "__main__":
    # Tworzenie obiektów
    a, b, c, d = Figura(), Prostokat(2, 4), Kwadrat(2), Kolo(3)

    # Wywołania funkcji pole
    print(f"Pole prostokąta (2x4): {pole(b)}")
    print(f"Pole kwadratu (bok=2): {pole(c)}")
    print(f"Pole koła (r=3): {pole(d)}")

    # Zmiana wymiarów za pomocą funkcji pole
    print(f"Pole prostokąta po zmianie na 5x6: {pole(b, 5, 6)}")
    print(f"Pole kwadratu po zmianie boku na 7: {pole(c, 7)}")
    print(f"Pole koła po zmianie promienia na 4: {pole(d, 4.0)}")

    # Polimorfizm
    polaPowierzchni([a, b, c, d])
