
from exceptions import SoldeInsuffisantException, MontantNegatifException

class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        if montant <= 0:
            raise MontantNegatifException("Impossible de déposer un montant négatif ou nul.")
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException("Solde insuffisant pour ce retrait.")
        self.solde -= montant

    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self.solde}€")
