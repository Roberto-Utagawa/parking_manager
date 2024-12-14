from models.enums import UserType

class Usuario:
    def __init__(self, id, nome, email, tipo: UserType, telefone):
        self.ID = id
        self.nome = nome
        self.email = email
        self.tipo = tipo
        self.telefone = telefone

    # Pagar
    # Fazer reserva
    # Cancelar Reserva

class UsuarioAdmin(Usuario):
    def __init__(self, id, nome, nivel_acesso, login, senha):
        super().__init__(id, nome, None, None, None)
        self.nivelDeAcesso = nivel_acesso
        self.login = login
        self.senha = senha

    # Cadastrar funcionario
    # Remover Funcionario
    # Cadastrar Vaga
    # Remover Vaga 
    # Ver Relatorio de Uso

class Funcionario:
    def __init__(self, id, nome, cargo, login, senha):
        self.ID = id
        self.nome = nome
        self.cargo = cargo
        self.login = login
        self.senha = senha

    # Controle de Entrada e Saida
    # Cadastrar Usuario
    # Remover Usuario