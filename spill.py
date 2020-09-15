import random
class spill:
    historie = []
    def spill_random(self):
        play = random.randint(0, 2)
        if play == 0:
            return "stein"
        elif play == 1:
            return "saks"
        else:
            return "papir"

    def motta_resultat(self, int, res):
        self.historie.append(res)
        if int == 1:
            self.poeng += 1
        elif int == -1:
            self.poeng += 0
        else:
            self.poeng += 0.5

    def oppgi_navn(self, name):
        self.name = name
        return True
