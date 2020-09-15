from spill import *
class tilfeldig:
    poeng = 0
    navn = "tilfeldig"
    historie = []

    def __init__(self):
        poeng = 0
        navn = "tilfeldig"
        historie = []

    def velg_aksjon(self):
        play = random.randint(0, 2)
        if play == 0:
            return "stein"
        elif play == 1:
            return "saks"
        else:
            return "papir"


    def oppgi_navn(self):
        return self.navn

    def motta_resultat(self, int, res):
        self.historie.append(res)
        if int == 1:
            self.poeng += 1
        elif int == -1:
            self.poeng += 0
        else:
            self.poeng += 0.5

    def get_poeng(self):
        return self.poeng
