import random
from spill import *
class mest_vanlig:
    poeng = 0
    historie = []
    navn = "mest vanlig"

    def velg_aksjon(self):
            antall_stein = 0
            antall_saks = 0
            antall_papir = 0
            for i in self.historie:
                if i == "saks":
                    antall_saks += 1
                elif i == "stein":
                    antall_stein += 1
                else:
                    antall_papir += 1
            if antall_saks > antall_papir and antall_saks > antall_stein:
                return "stein"
            elif antall_saks < antall_papir and antall_papir > antall_stein:
                return "saks"
            elif antall_stein > antall_papir and antall_saks < antall_stein:
                return  "papir"
            else:
                return "papir"

    def oppgi_navn(self):
        return self.navn

    def motta_resultat(self, int, res):
        self.historie.append(res)
        if int == 1:
            self.poeng += 1
        elif int == -1:
            self.poeng +=0
        else:
            self.poeng += 0.5

    def get_poeng(self):
        return self.poeng
