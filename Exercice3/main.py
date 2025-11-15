
from csv_reader import charger_csv, FichierIntrouvableException, LigneInvalideException, PrixNegatifException

def main():
    chemin = "articles.csv"  

    try:
        articles = charger_csv(chemin)
        print("Import réussi !")
        for article in articles:
            print(article)

    except FichierIntrouvableException as e:
        print(" Erreur : fichier introuvable.")
        print(e)

    except LigneInvalideException as e:
        print(" Erreur : une ligne du fichier est invalide.")
        print(e)

    except PrixNegatifException as e:
        print(" Erreur : un prix est invalide.")
        print(e)

    except Exception as e:
        print(" Erreur inconnue.")
        print(e)

if __name__ == "__main__":
    main()
