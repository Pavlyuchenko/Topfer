class Datum:
    def __init__(self, den, mesic, rok):
        self.den = den
        self.mesic = mesic
        self.rok = rok

    def __sub__(self, other):
        if self > other:
            prestupne_dny = 0
            for i in range(self.rok - other.rok):
                curr_rok = other.rok + i
                if curr_rok > 1582:
                    if curr_rok % 4 == 0 and not curr_rok % 100 == 0:
                        prestupne_dny += 1
                    elif curr_rok % 400 == 0:
                        prestupne_dny += 1
            dny = 0
            dny += (self.rok - other.rok) * 365

            
                    
        else:
            pass

    def __gt__(self, other):
        if self.rok > other.rok:
            return True
        elif self.rok < other.rok:
            return False
        else:
            if self.mesic > other.mesic:
                return True
            elif self.mesic < other.mesic:
                return False
            else:
                if self.den > other.den:
                    return True
                else:
                    return False


first = Datum(15, 12, 2002)
second = Datum(14, 12, 2002)

print(first>second)