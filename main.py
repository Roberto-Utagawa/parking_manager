from models.enums import UserType, StatusVaga
from models.usuarios import Usuario, UsuarioAdmin
from models.reserva import GerenciadorDeReservas
from models.vaga import GerenciadorDeVagas, Vaga

def main():
    # Instancia o gerenciador de vagas
    gerenciador_vagas = GerenciadorDeVagas()

    # Criar Vagas
    gerenciador_vagas.criar_vaga(1, "A1")
    gerenciador_vagas.criar_vaga(2, "A2")
    gerenciador_vagas.criar_vaga(1, "A3")  # Tenta criar vaga com ID duplicado

    # Visualizar Vagas
    gerenciador_vagas.ver_vagas()

    gerenciador_reservas = GerenciadorDeReservas()

    # Reservar Vagas
    gerenciador_reservas.reservar_vaga("usuario1", gerenciador_vagas.buscar_vaga_por_id(1))
    gerenciador_reservas.reservar_vaga("usuario2", gerenciador_vagas.buscar_vaga_por_id(2))
    gerenciador_reservas.reservar_vaga("usuario1", gerenciador_vagas.buscar_vaga_por_id(1))  # Tenta reservar vaga já ocupada

    # Visualizar Reservas
    gerenciador_reservas.ver_reservas()

    # Remover Reserva
    gerenciador_reservas.remover_reserva(1)
    gerenciador_reservas.ver_reservas()

    # Tentar remover uma reserva inexistente
    gerenciador_reservas.remover_reserva(99)

    
    print("\n==== SISTEMA ENCERRADO ====")

if __name__ == "__main__":
    main()
