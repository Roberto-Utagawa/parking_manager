from enum import Enum

class UserType(Enum):
    COMUM = "comum"
    VIP = "VIP"

class StatusVaga(Enum):
    LIVRE = "livre"
    OCUPADA = "ocupada"
    RESERVADA = "reservada"