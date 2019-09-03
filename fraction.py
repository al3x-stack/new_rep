def cmn_denom(num, denom):
    while num % denom != 0:
        old_num = num
        old_denon = denom
        num = old_denon
        denom = old_num % old_denon
    return denom


class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + " / " + str(self.denom)

    def __add__(self, other):
        new_num = self.num * other.denom + self.denom * other.num
        new_den = self.denom * other.denom
        common_den = cmn_denom(new_num, new_den)
        return Fraction(new_num // common_den, new_den // common_den)

    def __sub__(self, other):
        new_num = self.num * other.denom - self.denom * other.num
        new_den = self.denom * other.denom
        common_den = cmn_denom(new_num, new_den)
        return Fraction(new_num // common_den, new_den // common_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.denom * other.denom
        common_den = cmn_denom(new_num, new_den)
        return Fraction(new_num // common_den, new_den // common_den)

    def __truediv__(self, other):
        new_num = self.num * other.denom
        new_den = self.denom * other.num
        common_den = cmn_denom(new_num, new_den)
        return Fraction(new_num // common_den, new_den // common_den)


if __name__ == '__main__':
    fraction1 = Fraction(4, 5)
    fraction2 = Fraction(1, 8)
    print(fraction1 + fraction2)
    print(fraction1 - fraction2)
    print(fraction1 * fraction2)
    print(fraction1 / fraction2)
