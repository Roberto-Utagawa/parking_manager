from django.shortcuts import render, redirect

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

def cadastrar_vaga(request):
    return render(request, 'cadastrar_vaga.html')

def remover_vaga(request):
    return render(request, 'remover_vaga.html')

def cadastrar_funcionario(request):
    return render(request, 'cadastrar_funcionario.html')

def cancelar_funcionario(request):
    return render(request, 'cancelar_funcionario.html')

def reservar_cliente(request):
    return render(request, 'reservar_cliente.html')

def cancelar_cliente(request):
    return render(request, 'cancelar_cliente.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def removercliente(request):
    return render(request, 'removercliente.html')

def vagasdisponiveis_cliente(request):
    return render(request, 'vagasdisponiveis_cliente.html')

def vagasdisponiveis_funcionario(request):
    return render(request, 'vagasdisponiveis_funcionario')

def remover_funcionario(request):
    return render(request, 'remover_funcionario.html')

