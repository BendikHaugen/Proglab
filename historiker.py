class historiker:
    spill = 1
    poeng = 0
    historie = []
    navn = "historiker"

    def __init__(self, int):
        self.spill = int
        poeng = 0
        historie = []
        navn = "historiker"

    def velg_aksjon(self):
        if self.spill == 1:
            return self.enkel()
        else:
            return self.dobbel()

    def dobbel(self):
        if len(self.historie) < 2:
            return "stein"
        subset = [self.historie[len(self.historie)-2], self.historie[len(self.historie)-1]]
        stein = 0
        saks = 0
        papir = 0
        print(subset)
        print(stein)
        print(saks)
        print(papir)
        for i in range(len(self.historie)):
            sub = [self.historie[i-1], self.historie[i]]
            if subset == sub:
                try:
                    valg = self.historie[i+1]
                    if valg == saks:
                        saks += 1
                    elif valg == stein:
                        stein += 1
                    else:
                        papir += 1
                except:
                    valg = self.historie[i]
                    if valg == saks:
                        saks += 1
                    elif valg == stein:
                        stein += 1
                    else:
                        papir += 1
        if(stein > saks and stein > papir):
            return "stein"
        elif (saks > stein and saks > papir):
            return "saks"
        else:
            return "papir"

    def enkel(self):
        if len(self.historie) < 1:
            return "stein"
        subset = self.historie[-1]
        stein = 0
        saks = 0
        papir = 0
        for i in range(len(self.historie)):
            sub = self.historie[i-1]
            if subset == sub:
                valg = self.historie[i]
                if valg == saks:
                    saks += 1
                elif valg == stein:
                    stein += 1
                else:
                    papir += 1
        if(stein > saks and stein > papir):
            return "stein"
        elif (saks > stein and saks > papir):
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
