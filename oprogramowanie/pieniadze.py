class PrzechowywaczMonet:
    def __init__(self):
        self._grosze = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0}
        self._zlotowki = {'1': 3, '2': 0, '5': 5, '10': 0, '20': 0, '50': 0}
        self._sumaPojemnika = 0

    def suma(self):
        """Suma monet w złotówkach"""
        sumaGroszy = 0
        sumaZlotowek = 0

        for key, value in self._grosze.items():
            sumaGroszy += int(key)*value
        sumaGroszy = sumaGroszy/100

        for key, value in self._zlotowki.items():
            sumaZlotowek += int(key)*value

        return sumaGroszy + sumaZlotowek


a = PrzechowywaczMonet()
print(a.suma())
