

from compte_bancaire import CompteBancaire
from exceptions import SoldeInsuffisantException, MontantNegatifException

try:
    compte = CompteBancaire("Alice", 100)
    compte.afficher()
    compte.retirer(150)
except SoldeInsuffisantException as e:
    print("Erreur:", e)

try:
    compte.deposer(-50)
except MontantNegatifException as e:
    print("Erreur:", e)
