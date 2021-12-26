from oprogramowanie import pieniadze as p


class Biletomat(p.PrzechowywaczMonet):
    def __init__(self):
        super().__init__()
        self._depozyt = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0,
                         '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0}

    def dodajDoDepozytu(self, rodzaj, ile):
        self._depozyt[rodzaj] = self._depozyt[rodzaj] + ile
        print(self._depozyt[rodzaj])

    def sumaDepo(self):  # to potem bedzie mozna nadpisac, sprobowac, dac suma
        """Zwraca sumę monet w złotówkach"""
        suma = 0

        for key, value in self._depozyt.items():
            suma += int(key)*value

        return suma/100
