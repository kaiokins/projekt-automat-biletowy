class PrzechowywaczMonet:
    def __init__(self):
        self._pieniadze = {'1': 0, '2': 3, '5': 0, '10': 0, '20': 0, '50': 0,
                           '100': 1, '200': 3, '500': 0, '1000': 0, '2000': 3, '5000': 0}
        self._sumaPojemnika = 0

    def suma(self):
        """Zwraca sumę monet w złotówkach"""
        suma = 0

        for key, value in self._pieniadze.items():
            suma += int(key)*value

        return suma/100
        # a = PrzechowywaczMonet()
        # print(a.suma())

    def wydajReszte(self, doWydania):
        moneta = list(self._pieniadze.keys())
        ilosc = list(self._ilosc.values())

        moneta.reverse()
        ilosc.reverse()
