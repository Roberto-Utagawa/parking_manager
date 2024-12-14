from models.enums import StatusVaga, UsoVaga
from datetime import datetime

class Vaga:
    def __init__(self, id, localizacao):
        self.ID = id
        self.localizacao = localizacao

    # Criar Vaga
    # Ver Vagas
    # Remover Vaga

    
class Reserva:
    def __init__(self, id, usuario, vaga, data_hora_reserva: datetime, status: str):
        self.ID = id
        self.usuario = usuario
        self.vaga = vaga
        self.dataHoraReserva = data_hora_reserva
        self.status = status
    
    # Reservar vagas
    # Ver Vagas