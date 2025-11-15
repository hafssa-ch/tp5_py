
class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CapaciteDepasseeException(ReservationException):
    pass

class NombreInvalideException(ReservationException):
    pass

class NomClientInvalideException(ReservationException):
    pass
