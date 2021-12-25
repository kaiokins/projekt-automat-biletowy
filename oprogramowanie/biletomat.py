import pieniadze as p


class Biletomat(p.PrzechowywaczMonet):
    def __init__(self):
        super().__init__()


a = Biletomat()
print(a.suma())
