from models.enums import UserType

class Usuario:
    def __init__(self, id, nome, email, tipo: UserType, telefone):
        self.ID = id
        self.nome = nome
        self.email = email
        self.tipo = tipo
        self.telefone = telefone
        self.login = login
        self.senha = senha

    # Método para fazer uma reserva
    def fazer_reserva(self, gerenciador_reservas, reserva_id, id_vaga, data_hora_reserva: datetime):
        gerenciador_reservas.criar_reserva(reserva_id, self.nome, id_vaga, data_hora_reserva)
        print(f"Reserva feita com sucesso para o usuário {self.nome}!")

    # Método para visualizar reservas do usuário
    def ver_reservas(self, gerenciador_reservas):
        print(f"Reservas do usuário {self.nome}:")
        encontrou = False
        for reserva in gerenciador_reservas.reservas:
            if reserva.usuario == self.nome:
                print(reserva)
                encontrou = True
        if not encontrou:
            print("Nenhuma reserva encontrada.")

    # Método para cancelar uma reserva
    def cancelar_reserva(self, gerenciador_reservas, reserva_id):
        for reserva in gerenciador_reservas.reservas:
            if reserva.ID == reserva_id and reserva.usuario == self.nome:
                gerenciador_reservas.remover_reserva(reserva_id)
                print(f"Reserva {reserva_id} cancelada com sucesso.")
                return
        print(f"Erro: Reserva {reserva_id} não encontrada para o usuário {self.nome}.")

    # Método para visualizar vagas disponíveis
    def ver_vagas_disponiveis(self, gerenciador_reservas):
        ver_vagas_disponiveis_para_reserva(gerenciador_reservas)

class Admin(Usuario):
    def __init__(self, id, nome, nivel_acesso, login, senha):
        super().__init__(id, nome, None, None, None)
        self.nivelDeAcesso = nivel_acesso
        self.login = login
        self.senha = senha
    
    # Herda todas os metodos da classe funcionario e usuario
    # Cadastrar funcionario
    # Remover Funcionario
    # Cadastrar Vaga
    # Remover Vaga 
    # Ver Relatorio de Uso
    # Cadastrar Usuario
    # Remover Usuario

class Funcionario:
    def __init__(self, id, nome, cargo, login, senha):
        self.ID = id
        self.nome = nome
        self.cargo = cargo
        self.login = login
        self.senha = senha

    # Herda todas os metodos da classe funcionario
    # Cadastrar Usuario
    # Remover Usuario