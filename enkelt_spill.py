from spill import *
class enkelt_spill:
    spiller1 = None
    spiller2 = None

    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2

    def __str__(self):
        return True

    def gjennomføre_spill(self):
        aksjon_en = self.spiller1.velg_aksjon()
        aksjon_to = self.spiller2.velg_aksjon()
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


