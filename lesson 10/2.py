# task 2 == done

class Coat:
    def __init__(self, v):
        self.v = v

    @property
    def calculation_of_tissue(self):
        return self.v / 6.5 + 0.5


class Suit:
    def __init__(self, h):
        self.h = h

    @property
    def calculation_of_tissue(self):
        return 2 * self.h + 0.3


if __name__ == '__main__':
    a = Coat(3)
    b = Suit(4)
    print(a.calculation_of_tissue)
    print(b.calculation_of_tissue)