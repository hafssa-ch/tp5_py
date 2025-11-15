
import os
from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

dossier = os.path.dirname(__file__)

def creer_csv(nom_fichier, lignes):
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))
    return chemin

chemin_valide = creer_csv("articles.csv", [
    "1;Stylo;2.5",
    "2;Cahier;3.0",
    "3;Gomme;1.2"
])

chemin_prix_non_num = creer_csv("prix_non_num.csv", [
    "1;Stylo;abc"
])

chemin_prix_negatif = creer_csv("prix_negatif.csv", [
    "1;Stylo;-5"
])

chemin_ligne_invalide = creer_csv("ligne_invalide.csv", [
    "1;Stylo"
])



def test_fichier_valide():
    print("Test : fichier valide")
    try:
        articles = charger_csv(chemin_valide)
        print(" Succès :", articles)
    except Exception as e:
        print(" Erreur inattendue :", e)

def test_fichier_absent():
    print("\nTest : fichier absent")
    try:
        charger_csv("inexistant.csv")
    except FichierIntrouvableException as e:
        print(" OK :", e)

def test_prix_non_numerique():
    print("\nTest : prix non numérique")
    try:
        charger_csv(chemin_prix_non_num)
    except PrixNegatifException as e:
        print(" OK :", e)

def test_prix_negatif():
    print("\nTest : prix négatif")
    try:
        charger_csv(chemin_prix_negatif)
    except PrixNegatifException as e:
        print(" OK :", e)

def test_ligne_invalide():
    print("\nTest : ligne invalide")
    try:
        charger_csv(chemin_ligne_invalide)
    except LigneInvalideException as e:
        print(" OK :", e)

if __name__ == "__main__":
    test_fichier_valide()
    test_fichier_absent()
    test_prix_non_numerique()
    test_prix_negatif()
    test_ligne_invalide()
