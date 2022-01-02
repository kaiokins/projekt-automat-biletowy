import csv


class PrzechowywaczMonet:
    def wczytajPlik(self):
        """Metoda odpowiedzialna za wczytywanie z pliku .csv rodzajów oraz ilości monet/banknotów"""
        try:
            with open('C:/Users/Kuba/Documents/GitHub/projekt-automat-biletowy/oprogramowanie/pieniadze.csv', mode='r') as f:
                reader = csv.reader(f)
                for row in reader:
                    k, v = row
                    self._pieniadze[str(k)] = int(v)
        except:
            print("Wystąpił błąd przy wczytywaniu pliku")
        finally:
            f.close()

    def zapiszPlik(self):
        """Metoda odpowiedzialna za zapisywanie do pliku ilości monet/banknotów po poprawnym wykonaniu wszystkich operacji transakcyjnych"""
        try:
            with open('C:/Users/Kuba/Documents/GitHub/projekt-automat-biletowy/oprogramowanie/pieniadze.csv', mode='w') as f:
                [f.write('{0},{1}\n'.format(key, value))
                 for key, value in self._pieniadze.items()]
        except:
            print("Wystąpił błąd przy zapisywaniu pliku")
        finally:
            f.close()

    def __init__(self):
        """
        Klasa PrzechowywaczMonet służy do przechowywania rodzajów oraz ilości monet/banknotów. Posiada metody odpowiedzialne za zapisanie oraz wczytanie monet/banknotów.
        """
        self._pieniadze = {} # Pojemnik (w postaci słownika) służący do przechowywania monet/banknotów (rodzaj:ilość)
        # self._pieniadze = {'1': 55, '2': 55, '5': 55, '10': 55, '20': 55, '50': 55, '100': 55, '200': 55, '500': 55, '1000': 55, '2000': 55, '5000': 55}
        self._sumaPojemnika = 0
        self._doUsunieciaZPrzechowywacza = 0
        self.wczytajPlik() # Wywołanie funkcji wczytującej monety/banknoty

    def suma(self):
        """Zwraca sumę monet w złotówkach"""
        suma = 0

        for key, value in self._pieniadze.items():
            suma += int(key)*value

        return suma/100
        # a = PrzechowywaczMonet()
        # print(a.suma())

    def wydajReszte(self, doWydania):
        """Metoda odpowiedzialna za wydawanie reszty"""

        # Na poczatku rozdzielam rodzaj oraz ilość na dwie zmienne
        moneta = list(self._pieniadze.keys())
        ilosc = list(self._pieniadze.values())

        # Odwracam słownik by wartości były segregowane od największej do najmniejszej.
        # Jeśli ktoś zakupi bilet za 6 złotych i zapłaci 50 złotową monetą do należy sprawdzić
        # w późniejszych etapach czy można mu wydać jak największymi nominałami.
        moneta.reverse()
        ilosc.reverse()

        #Przez to, że 
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
