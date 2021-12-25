from oprogramowanie import pieniadze as p


class Biletomat(p.PrzechowywaczMonet):
    def __init__(self):
        super().__init__()
        self._depozytGroszy = {'1': 0, '2': 0,
                               '5': 0, '10': 0, '20': 0, '50': 0}
        self._depozytZlotowek = {'1': 0, '2': 0,
                                 '5': 0, '10': 0, '20': 0, '50': 0}

    def wplacMonety(self, gr1, gr2, gr5, gr10, gr20, gr50, zl1, zl2, zl5, zl10, zl20, zl50):
        print("elo")
