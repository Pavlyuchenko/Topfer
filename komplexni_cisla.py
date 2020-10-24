class Komplexni:
    def __init__(self, imaginarni, realna):
        self.imaginarni = imaginarni
        self.realna = realna

    def __add__(self, other):
        return str(self.imaginarni + other.imaginarni) + "i + " + str(self.realna + other.realna)

    def __mul__(self, other):
        return str(self.imaginarni * other.imaginarni) + "i + " + str(self.realna * other.realna)

a = Komplexni(4, 3)
b = Komplexni(2, 8)

print(a * b)