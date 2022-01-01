class bladUjemnaWartosc(Exception):
    def __init__(self, wiadomosc):
        self._wiadomosc = wiadomosc

class bladZapisywaniaPliku(Exception):
    def __init__(self, wiadomosc):
        self._wiadomosc = wiadomosc