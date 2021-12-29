import csv


class PrzechowywaczMonet:
    def wczytajPlik(self):
        try:
            f = csv.reader(
                open('C:/Users/Kuba/Documents/GitHub/projekt-automat-biletowy/pieniadze.csv'))
            self._pieniadze = dict(f)
            for i in self._pieniadze.keys():
                self._pieniadze[i] = int(self._pieniadze[i])
            print("ZAIMPORTOWANE: ", self._pieniadze)
        except:
            print("Nie udało się wczytaj pliku")
        f.close()

    def zapiszPlik(self):

        with open('C:/Users/Kuba/Documents/GitHub/projekt-automat-biletowy/pieniadze.csv', "w") as f:
            zapis = csv.writer(f)
            for key, value in self._pieniadze.items():
                zapis.writerow([key, value])
            print("ZAPISANE")

    def __init__(self):
        self._pieniadze = {}
        # self._pieniadze = {'1': 55, '2': 55, '5': 55, '10': 55, '20': 55, '50': 55, '100': 55, '200': 55, '500': 55, '1000': 55, '2000': 55, '5000': 55}
        self._sumaPojemnika = 0
        self._doUsunieciaZPrzechowywacza = 0
        self.wczytajPlik()

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
        ilosc = list(self._pieniadze.values())

        moneta.reverse()
        ilosc.reverse()
        doWydania = doWydania*100
        reszta = [0] * 12
        print('ILE DO WYDANIA', doWydania)
        for i in range(12):
            while not ((int(moneta[i])) > doWydania) and ilosc[i] > 0:
                doWydania -= int(moneta[i])
                ilosc[i] -= 1
                reszta[i] += 1
                print("TYLE ODJĄŁ", moneta[i])
            print("TU", doWydania)

        moneta.reverse()
        ilosc.reverse()
        reszta.reverse()

        zostalo = dict(zip(moneta, ilosc))
        reszta = dict(zip(moneta, reszta))
        print("zostalo", zostalo)
        print("reszta", reszta)

        if doWydania == 0:
            self._pieniadze = zostalo
            return (zostalo, reszta)
        else:
            return -1
