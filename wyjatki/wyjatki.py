# W pliku wyjątki definiujemy klasy wyjątków używane w pozostałych fragmentach programu

class bladUjemnaWartosc(Exception):
    def __init__(self, wiadomosc):
        """
        Klasa wyjątku, która użyta jest przy sprawdzaniu poprawności wprowadzenia liczby biletów/ilości monet lub banknotów.
        Wywoływana jest w momencie wprowadzenai liczby mniejszej niż 0 przez użytkownika. Wysyła ona wiadomość na ekranie konsoli
        z informacją o błędzie dla administratora.
        """
        self._wiadomosc = wiadomosc