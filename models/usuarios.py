class Usuario:
    def __init__(self, id, nome, email):
        self.ID = id
        self.nome = nome
        self.login = login
        self.senha = senha

    # Método para fazer uma reserva
    def fazer_reserva(self, gerenciador_reservas, id_vaga, data_hora_reserva: datetime):
        gerenciador_reservas.criar_reserva( self.nome, id_vaga, data_hora_reserva)
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
    def ver_vagas_disponiveis(self, gerenciador_
    reservas):
        ver_vagas_disponiveis_para_reserva(gerenciador_reservas)

class Admin(Usuario):
    def __init__(self, id, nome, login, senha):
        super().__init__(id, nome, "admin", "admin")
        self.login = login
        self.senha = senha

    # Método para cadastrar um novo funcionário
    def cadastrar_funcionario(self, lista_funcionarios, id, nome, cargo, login, senha):
        for funcionario in lista_funcionarios:
            if funcionario.ID == id:
                print(f"Erro: Funcionário com ID {id} já existe.")
                return
        novo_funcionario = Funcionario(id, nome, cargo, login, senha)
        lista_funcionarios.append(novo_funcionario)
        print(f"Funcionário {nome} cadastrado com sucesso pelo administrador {self.nome}.")

    # Método para remover um funcionário
    def remover_funcionario(self, lista_funcionarios, id_funcionario):
        for funcionario in lista_funcionarios:
            if funcionario.ID == id_funcionario:
                lista_funcionarios.remove(funcionario)
                print(f"Funcionário {funcionario.nome} removido com sucesso pelo administrador {self.nome}.")
                return
        print(f"Erro: Funcionário com ID {id_funcionario} não encontrado.")

    # Método para cadastrar uma nova vaga
    def cadastrar_vaga(self, gerenciador_vagas, id, localizacao):
        gerenciador_vagas.criar_vaga(id, localizacao)
        print(f"Vaga {localizacao} cadastrada com sucesso pelo administrador {self.nome}.")

    # Método para remover uma vaga
    def remover_vaga(self, gerenciador_vagas, id_vaga):
        vaga = gerenciador_vagas.buscar_vaga_por_id(id_vaga)
        if not vaga:
            print(f"Erro: Vaga com ID {id_vaga} não encontrada.")
            return
        gerenciador_vagas.vagas.remove(vaga)
        print(f"Vaga {vaga.localizacao} removida com sucesso pelo administrador {self.nome}.")

    # Método para gerar um relatório de uso
    def ver_relatorio_uso(self, gerenciador_vagas, gerenciador_reservas):
        total_vagas = len(gerenciador_vagas.vagas)
        vagas_ocupadas = sum(1 for vaga in gerenciador_vagas.vagas if vaga.status == StatusVaga.OCUPADA)
        vagas_reservadas = sum(1 for vaga in gerenciador_vagas.vagas if vaga.status == StatusVaga.RESERVADA)
        vagas_livres = total_vagas - (vagas_ocupadas + vagas_reservadas)

        print("Relatório de Uso:")
        print(f"Total de vagas: {total_vagas}")
        print(f"Vagas ocupadas: {vagas_ocupadas}")
        print(f"Vagas reservadas: {vagas_reservadas}")
        print(f"Vagas livres: {vagas_livres}")

        print("\nDetalhes das Reservas:")
        for reserva in gerenciador_reservas.reservas:
            print(reserva)

    # Método para herdar funcionalidades do Usuario e Funcionario
    def herdar_metodos_usuario_funcionario(self, **kwargs):
        # Pode chamar métodos específicos de ambas as classes
        pass

class Funcionario:
    def __init__(self, id, nome, cargo, login, senha):
        self.ID = id
        self.nome = nome
        self.cargo = cargo
        self.login = login
        self.senha = senha

    # Método para remover uma reserva de um usuário
    def remover_reserva_usuario(self, gerenciador_reservas, id_reserva):
        for reserva in gerenciador_reservas.reservas:
            if reserva.ID == id_reserva:
                # Libera a vaga reservada
                gerenciador_reservas.gerenciador_vagas.alterar_status(
                    reserva.vaga.ID, StatusVaga.LIVRE
                )
                gerenciador_reservas.reservas.remove(reserva)
                print(f"Reserva {id_reserva} removida com sucesso!")
                return
        print(f"Erro: Reserva com ID {id_reserva} não encontrada.")

    # Método para criar uma reserva para um usuário
    def criar_reserva_usuario(self, gerenciador_reservas, usuario, id_vaga, data_hora_reserva):
        gerenciador_reservas.criar_reserva(usuario.nome, id_vaga, data_hora_reserva)

    # Método para cadastrar um novo usuário
    def cadastrar_usuario(self, usuarios, id, nome, email, tipo, telefone):
        for usuario in usuarios:
            if usuario.ID == id:
                print(f"Erro: Usuário com ID {id} já existe.")
                return
        novo_usuario = Usuario(id, nome, email, tipo, telefone)
        usuarios.append(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")

    # Método para remover um usuário
    def remover_usuario(self, usuarios, id_usuario):
        for usuario in usuarios:
            if usuario.ID == id_usuario:
                usuarios.remove(usuario)
                print(f"Usuário {usuario.nome} removido com sucesso!")
                return
        print(f"Erro: Usuário com ID {id_usuario} não encontrado.")

    # Método para visualizar todas as reservas
    def ver_todas_as_reservas(self, gerenciador_reservas):
        if not gerenciador_reservas.reservas:
            print("Nenhuma reserva cadastrada.")
            return
        print("Lista de Reservas:")
        for reserva in gerenciador_reservas.reservas:
            print(reserva)

    # Método para visualizar vagas disponíveis
    def ver_vagas_disponiveis(self, gerenciador_vagas):
        vagas_disponiveis = [
            vaga for vaga in gerenciador_vagas.vagas if vaga.status == StatusVaga.LIVRE
        ]
        if not vagas_disponiveis:
            print("Nenhuma vaga disponível.")
            return
        print("Vagas Disponíveis:")
        for vaga in vagas_disponiveis:
            print(vaga)