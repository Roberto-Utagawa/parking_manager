from enum import Enum

class UserType(Enum):
    COMUM = "Comum"
    VIP = "VIP"

class StatusVaga(Enum):
    LIVRE = "Livre"
    OCUPADA = "Ocupada"
    RESERVADA = "Reservada"