from models.enums import UserType, StatusVaga
from models.usuarios import Usuario, Admin, Funcionario
from models.reserva import GerenciadorDeReservas
from models.vaga import GerenciadorDeVagas, Vaga
from datetime import datetime

def main():

    # Instancia o gerenciador de vagas
    gerenciador_vagas = GerenciadorDeVagas()
    # Instancia o gerenciador de reservas
    gerenciador_reservas = GerenciadorDeReservas(gerenciador_vagas)
    # Instancia do admin
    admin = Admin(0, "admin", "admin", "admin")


    # Visualizar Vagas
    gerenciador_vagas.ver_vagas()

    admin.cadastrar_vaga(gerenciador_vagas, 0, 0)
    # admin.remover_vaga()
    # gerenciador_vagas.ver_vagas()

    usuario = Usuario("user", 0, "teste", "teste")
    usuario.ver_vagas_disponiveis(gerenciador_reservas)

    # Visualizar Reservas
    # gerenciador_reservas.ver_reservas()

    # print("\n==== REMOVENDO VAGA ====")
    # # Remover Reserva
    # gerenciador_reservas.cancelar_reserva(1)
    # gerenciador_reservas.ver_reservas()

    # # Tentar remover uma reserva inexistente
    # gerenciador_reservas.cancelar_reserva(99)

    
    print("\n==== SISTEMA ENCERRADO ====")

if __name__ == "__main__":
    main()
