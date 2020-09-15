class sekvensiell:
    spill = ["stein", "saks", "papir"]
    poeng = 0
    last_pos = -1
    navn = "sekvensiell"
    historie = []

    def oppgi_navn(self):
        return self.navn

    def oppdater_score(self, int):
        if int == 0:
            self.poeng += 0.5
        elif int == 1:
            self.poeng += 1

    def velg_aksjon(self):
        if self.last_pos == 2:
            self.last_pos = -1
        self.last_pos += 1
        return self.spill[self.last_pos]

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
