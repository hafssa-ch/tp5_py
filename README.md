# TP5 – Gestion des Exceptions et Validation en Python

Ce TP comprend 3 exercices centrés sur la gestion des exceptions personnalisées et la validation des données en Python.

## Exercice 1 – Compte bancaire

### Objectif pédagogique :
Apprendre à créer des exceptions personnalisées pour gérer des cas métiers spécifiques (retraits et dépôts).

### Fonctionnalités :

Classe CompteBancaire avec méthodes : deposer(), retirer(), afficher().

Exceptions personnalisées :
SoldeInsuffisantException : levée si le retrait dépasse le solde.
MontantNegatifException : levée si le dépôt est nul ou négatif.

### Fichiers :
exceptions.py : contient les exceptions.
compte_bancaire.py : classe CompteBancaire.
main.py : point d’entrée pour tester le compte.
<img width="1641" height="164" alt="image" src="https://github.com/user-attachments/assets/6a89aa17-f52d-4d62-8e8e-757e5d601606" />

## Exercice 2 – Réservation d’événement

### Objectif pédagogique :
Gérer plusieurs types d’exceptions dans un système de réservation et appliquer des validations métier robustes.

### Fonctionnalités :
Classe Evenement avec méthodes : reserver(), afficher().
Exceptions personnalisées :
ReservationException : exception de base.
CapaciteDepasseeException : si réservation > capacité.
NombreInvalideException : si nombre de places <= 0.
NomClientInvalideException : si nom client vide.

### Fichiers :
exceptions_reservation.py : contient les exceptions.
evenement.py : classe Evenement.
main_reservation.py : point d’entrée pour tester les réservations.
<img width="1639" height="205" alt="image" src="https://github.com/user-attachments/assets/c1928174-74ea-41b5-88e5-dbe59871d4a7" />

## Exercice 3 – Import CSV sécurisé

### Objectif pédagogique :
Renforcer la maîtrise des exceptions personnalisées appliquées à la lecture et validation de fichiers CSV.

### Fonctionnalités :
Fonction charger_csv(chemin) qui renvoie une liste de dictionnaires {id, nom, prix}.
Exceptions personnalisées :
CsvException : exception de base.
FichierIntrouvableException : si le fichier n’existe pas.
LigneInvalideException : si une ligne ne comporte pas exactement 3 colonnes.
PrixNegatifException : si le prix n’est pas numérique ou <= 0.

### Fichiers :
csv_reader.py : fonctions et exceptions.
main.py : point d’entrée pour tester l’import CSV.
test_manuel.py : tests manuels pour tous les cas (fichier valide, absent, ligne invalide, prix non numérique ou négatif).
<img width="1636" height="567" alt="image" src="https://github.com/user-attachments/assets/8221dbda-9c89-4506-8e71-ce079aca4f89" />
