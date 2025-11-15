# csv_reader.py

import os

# Exceptions personnalisées
class CsvException(Exception):
    pass

class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass

# Fonction pour charger le CSV
def charger_csv(chemin):
    if not os.path.exists(chemin):
        raise FichierIntrouvableException(f"Fichier introuvable : {chemin}")

    articles = []
    with open(chemin, "r", encoding="utf-8") as f:
        for num, ligne in enumerate(f, start=1):
            ligne = ligne.strip()
            if not ligne:
                continue
            colonnes = ligne.split(";")
            if len(colonnes) != 3:
                raise LigneInvalideException(f"Ligne {num} invalide : {ligne}")
            id_str, nom, prix_str = colonnes
            try:
                prix = float(prix_str)
            except ValueError:
                raise PrixNegatifException(f"Prix non numérique à la ligne {num} : '{prix_str}'")
            if prix <= 0:
                raise PrixNegatifException(f"Prix négatif ou nul à la ligne {num} : {prix}")
            articles.append({"id": id_str, "nom": nom, "prix": prix})
    return articles
