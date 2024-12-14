from models.enums import UserType, StatusVaga
from models.usuarios import Usuario, UsuarioAdmin
from models.interface import iniciar_interface


def main():

    iniciar_interface()
    # Criação de Usuários
    print("==== CRIANDO USUÁRIOS ====")
    usuario1 = Usuario(1, "João Silva", "joao@email.com", UserType.COMUM, "11999999999")
    admin1 = UsuarioAdmin(2, "Administrador", "Nível 1", "admin", "admin123")
    print(f"Usuário: {usuario1.nome}, Tipo: {usuario1.tipo}")
    print(f"Admin: {admin1.nome}, Acesso: {admin1.nivelDeAcesso}")

    
    print("\n==== SISTEMA ENCERRADO ====")

if __name__ == "__main__":
    main()

