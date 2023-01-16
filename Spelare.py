from Svärd import *

class Spelare:
    def __init__(self, liv, styrka,gubbe_typ):
        self.liv = liv
        self.styrka = styrka
        self.nivå = 1
        self.grejer = [Svärd("a",1), Svärd("b",1), Svärd("c",1), Svärd("d",1), Svärd("e",1)]
        self.gubbe_typ= gubbe_typ
    #Grejer är en lista på svärden
#Det här kommer printas när det står print("Karaktär")
    def __str__(self):
        return f"\nDu är {self.gubbe_typ},Ditt liv är {self.liv}, din Styrka är {self.styrka}, din styrka tillsamans med dina vapen är {self.total_styrka()}, din nivå är {self.nivå}"

    def visa_rygga(self):
        if len(self.grejer) == 0:
            print("\nJust nu är din ryggsäck tom")
        for i in range(len(self.grejer)):
            print(f"\n{(i+1)}: Namn = {self.grejer[i].namn} Styrka = {self.grejer[i].svärd_styrka}")

    def total_styrka(self):
        y= self.styrka
        for i in range(len(self.grejer)):
            y+=self.grejer[i].svärd_styrka
        return y

    def om_fälla(self):
        self.liv -=1
        print("\nDu ramlade in i en fälla och tog 1 skada. \n"
            f"Ditt liv är nu {self.liv}")
