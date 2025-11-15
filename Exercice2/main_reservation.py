from evenement import Evenement
from exceptions_reservation import ReservationException

event = Evenement("Concert", 5)

# Cas 1 : nom vide
try:
    event.reserver("", 2)
except ReservationException as e:
    print("Erreur:", e)

# Cas 2 : nombre de places négatif
try:
    event.reserver("Alice", -1)
except ReservationException as e:
    print("Erreur:", e)

# Cas 3 : capacité dépassée
try:
    event.reserver("Bob", 6)
except ReservationException as e:
    print("Erreur:", e)

# Cas 4 : réservation valide
try:
    event.reserver("Charlie", 3)
    event.afficher()
except ReservationException as e:
    print("Erreur:", e)
