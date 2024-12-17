from models.enums import StatusVaga
from models.vaga import GerenciadorDeVagas, Vaga
from datetime import datetime

from datetime import datetime

class Reserva:
    def __init__(self, id, usuario, vaga, data_hora_reserva: datetime):
        self.ID = id
        self.usuario = usuario
        self.vaga = vaga
        self.dataHoraReserva = data_hora_reserva

    def __str__(self):
        return (f"ID: {self.ID}, Usuário: {self.usuario}, "
                f"Vaga: {self.vaga.localizacao}, Data: {self.dataHoraReserva}")


class GerenciadorDeReservas:
    def __init__(self, gerenciador_vagas):
        self.reservas = []  # Lista para armazenar reservas
        self.gerenciador_vagas = gerenciador_vagas  # Referência ao gerenciador de vagas
        self.countReservas = 0

    # Método para criar uma reserva
    def criar_reserva(self, usuario, id_vaga, data_hora_reserva: datetime):

        # Verifica se a vaga existe
        vaga = self.gerenciador_vagas.buscar_vaga_por_id(id_vaga)
        if not vaga:
            print(f"Erro: Vaga com ID {id_vaga} não encontrada.")
            return

        # Verifica se a vaga está livre
        if vaga.status != StatusVaga.LIVRE:
            print(f"Erro: Vaga {id_vaga} não está disponível para reserva.")
            return

        # Cria a reserva
        id = self.countReservas
        self.countReservas += 1

        nova_reserva = Reserva(id, usuario, vaga, data_hora_reserva)
        self.reservas.append(nova_reserva)

        # Atualiza o status da vaga para "Reservada"
        self.gerenciador_vagas.alterar_status(id_vaga, StatusVaga.RESERVADA)
        print(f"Reserva criada com sucesso: {nova_reserva}")


    # Método para visualizar todas as reservas
    def ver_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva cadastrada.")
            return

        print("Lista de Reservas:")
        for reserva in self.reservas:
            print(reserva)


    # Método para buscar uma reserva pelo ID
    def buscar_reserva_por_id(self, id):
        for reserva in self.reservas:
            if reserva.ID == id:
                return reserva
        print(f"Erro: Reserva com ID {id} não encontrada.")
        return None


    # Método para cancelar uma reserva
    def cancelar_reserva(self, id):
        reserva = self.buscar_reserva_por_id(id)
        if not reserva:
            return

        # Atualiza o status da vaga para "Livre"
        self.gerenciador_vagas.alterar_status(reserva.vaga.ID, StatusVaga.LIVRE)

        # Remove a reserva da lista
        self.reservas.remove(reserva)
        print(f"Reserva cancelada com sucesso: ID {id}")

    def ver_vagas_disponiveis_para_reserva(self):
        print("Vagas disponíveis:")
        encontrou = False
        for vaga in self.gerenciador_vagas.vagas:
            if vaga.status == StatusVaga.LIVRE:
                print(vaga)
                encontrou = True
        if not encontrou:
            print("Nenhuma vaga disponível.")