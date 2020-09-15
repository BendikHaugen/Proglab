from enkelt_spill import *
import matplotlib.pyplot as plt
from tilfeldig import *
from historiker import *
from sekvensiell import *
from mestvanlig import *
class mange_spill:
    spiller1 = None
    spiller2 = None
    antall_spill = 0


    def __init__(self, spiller1, spiller2, antall_spill):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall_spill = antall_spill

    def gjennomfør_enkeltspill(self):
        aksjon_en = self.spiller1.velg_aksjon()
        aksjon_to = self.spiller2.velg_aksjon()
        print(aksjon_en)
        print(aksjon_to)
        if aksjon_en == "saks":
            if aksjon_to == "papir":
                self.spiller1.motta_resultat(1, "papir")
                self.spiller2.motta_resultat(-1, "saks")
            elif aksjon_to == "stein":
                self.spiller2.motta_resultat(1, "saks")
                self.spiller1.motta_resultat(-1, "stein")
            else:
                self.spiller1.motta_resultat(0, "saks")
                self.spiller2.motta_resultat(0, "saks")
        elif aksjon_en == "stein":
            if aksjon_to == "saks":
                self.spiller1.motta_resultat(1, "saks")
                self.spiller2.motta_resultat(-1, "stein")
            elif aksjon_to == "papir":
                self.spiller2.motta_resultat(1, "stein")
                self.spiller1.motta_resultat(-1, "papir")
            else:
                self.spiller1.motta_resultat(0, "stein")
                self.spiller2.motta_resultat(0, "stein")
        else:
            if aksjon_to == "stein":
                self.spiller1.motta_resultat(1, "stein")
                self.spiller2.motta_resultat(-1, "papir")
            elif aksjon_to == "saks":
                self.spiller2.motta_resultat(1, "papir")
                self.spiller1.motta_resultat(-1, "saks")
            else:
                self.spiller1.motta_resultat(0, "papir")
                self.spiller2.motta_resultat(0, "papir")

    def gjennomfør_turnering(self):
        n = 0
        seiersprosent = []
        while self.antall_spill > 0:
            n += 1
            self.antall_spill -=1
            self.gjennomfør_enkeltspill()
            seiersprosent.append(self.spiller1.get_poeng() / n)
        plt.plot(seiersprosent)
        plt.ylabel('seiersprosent')
        plt.show()
