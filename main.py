from models.enums import UserType, StatusVaga
from models.usuarios import Usuario, UsuarioAdmin
from models.reserva import GerenciadorDeReservas
from models.vaga import GerenciadorDeVagas, Vaga
from datetime import datetime

def main():
    # Instancia o gerenciador de vagas
    gerenciador_vagas = GerenciadorDeVagas()

    # Criar Vagas
    gerenciador_vagas.criar_vaga(1, "A1")
    gerenciador_vagas.criar_vaga(2, "A2")
    gerenciador_vagas.criar_vaga(1, "A3")  # Tenta criar vaga com ID duplicado

    # Visualizar Vagas
    gerenciador_vagas.ver_vagas()

    gerenciador_reservas = GerenciadorDeReservas(gerenciador_vagas)

    # Reservar Vagas
    gerenciador_reservas.criar_reserva("João", 1, datetime.now())
    gerenciador_reservas.criar_reserva("Maria", 2, datetime.now())
    gerenciador_reservas.criar_reserva("Pedro", 1, datetime.now())

    # Visualizar Reservas
    gerenciador_reservas.ver_reservas()

    print("\n==== REMOVENDO VAGA ====")
    # Remover Reserva
    gerenciador_reservas.cancelar_reserva(1)
    gerenciador_reservas.ver_reservas()

    # Tentar remover uma reserva inexistente
    gerenciador_reservas.cancelar_reserva(99)

    
    print("\n==== SISTEMA ENCERRADO ====")

if __name__ == "__main__":
    main()
