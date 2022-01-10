class Blad(Exception):
    """Bazowa klasa wyjątków"""
    pass


class bladUjemnaWartosc(Blad):
    def __init__(self, wiadomosc):
        """
        Klasa wyjątku, która użyta jest przy sprawdzaniu poprawności wprowadzenia liczby biletów/ilości monet lub banknotów.
        Wywoływana jest w momencie wprowadzenia liczby mniejszej niż 0 przez użytkownika. Wysyła ona wiadomość na ekranie konsoli
        z informacją o błędzie dla administratora.
        """
        self._wiadomosc = wiadomosc
