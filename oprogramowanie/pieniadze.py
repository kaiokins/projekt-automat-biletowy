class PrzechowywaczMonet:
    def __init__(self):
        self._grosze = {'1': 8, '2': 0, '5': 0, '10': 2, '20': 0, '50': 0}
        self._zlotowki = {'1': 3, '2': 5, '5': 5, '10': 1, '20': 1, '50': 0}
        self._sumaPojemnika = 0

    def suma(self):
        """Zwraca sumę monet w złotówkach"""
        sumaGroszy = 0
        sumaZlotowek = 0

        for key, value in self._grosze.items():
            sumaGroszy += int(key)*value
        sumaGroszy = sumaGroszy/100

        for key, value in self._zlotowki.items():
            sumaZlotowek += int(key)*value

        self._sumaPojemnika = sumaGroszy + sumaZlotowek
        return sumaGroszy + sumaZlotowek


# a = PrzechowywaczMonet()
# print(a.suma())
