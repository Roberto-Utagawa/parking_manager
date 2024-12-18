from models.enums import UserType, StatusVaga
from models.usuarios import Usuario, Admin, Funcionario
from models.reserva import GerenciadorDeReservas
from models.vaga import GerenciadorDeVagas, Vaga
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def main():

    # Instancia o gerenciador de vagas
    gerenciador_vagas = GerenciadorDeVagas()
    # Instancia o gerenciador de reservas
    gerenciador_reservas = GerenciadorDeReservas(gerenciador_vagas)
    # Instancia do admin
    admin = Admin(0, "admin", "admin", "admin")


    usuarios = [
    Usuario(1, "Roberto", "roberto123", "senha123"),
    Usuario(2, "Ana", "ana456", "senha456"),
    Usuario(3, "Carlos", "carlos789", "senha789"),
    ]

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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')  # Obtém o tipo de usuário
        
        if user_type == 'admin':
            return redirect('homeAdmin')
        elif user_type == 'employee':
            return redirect('homeFuncionario')
        elif user_type == 'customer':
            # se estiver na lista de usuarios
            return redirect('homeCliente')
        else:
            return render(request, 'login.html', {'error': 'Tipo de usuário inválido'})

    return render(request, 'login.html')

def homeAdmin(request):
    return render(request, 'homeAdmin.html')

def homeFuncionario(request):
    return render(request, 'homeFuncionario.html')

def homeCliente(request):
    return render(request, 'homeCliente.html')

def reservar_funcionario(request):
    return render(request, 'reservar_funcionario.html')

def vagas(request):
    return render(request, 'vagas.html')

def funcionarios(request):
    return render(request, 'funcionarios.html')

def cancelar_funcionario(request):
    return render(request, 'cancelar_funcionario.html')

def reservar_cliente(request):
    return render(request, 'reservar_cliente.html')

def cancelar_cliente(request):
    return render(request, 'cancelar_cliente.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def vagasdisponiveis_cliente(request):
    return render(request, 'vagasdisponiveis_cliente.html')

def removercliente(request):
    return render(request, 'removercliente.html')