class bladUjemnaWartosc(Exception):
    def __init__(self, wiadomosc):
        self._wiadomosc = wiadomosc


class bladWczytywaniaPliku(Exception):
    def __init__(self, wiadomosc):
        self._wiadomosc = wiadomosc
