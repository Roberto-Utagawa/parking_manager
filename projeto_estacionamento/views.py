from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages  # Para exibir mensagens de erro
from .models import Cliente, Vaga, HistoricoDeUso
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        cpf = request.POST.get('username')  # Username será o CPF
        senha = request.POST.get('password')

        try:
            # Tenta buscar o cliente pelo CPF
            user = Cliente.objects.get(cpf=cpf)
            if check_password(senha, user.senha):  # Valida a senha
                # Redireciona de acordo com o tipo de cliente
                if user.tipo == "VIP":
                    return redirect('home_vip')  # Redireciona para a homepage VIP
                else:
                    return redirect('home_comum')  # Redireciona para a homepage comum
            else:
                # Exibe mensagem de senha incorreta
                messages.error(request, 'Senha incorreta.')
        except Cliente.DoesNotExist:
            # Exibe mensagem de CPF não encontrado
            messages.error(request, 'CPF não encontrado.')

    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')

        # Verificar se CPF já existe
        if Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado.')
        else:
            # Cria um novo usuário no banco
            Cliente.objects.create(
                nome=nome,
                cpf=cpf,
                email=email,
                telefone=telefone,
                senha=make_password(senha),
                tipo_usuario='Comum'  # Definindo o tipo como padrão
            )
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('cadastro')  # Volta para o cadastro, onde o pop-up será acionado

    return render(request, 'cadastro.html')

def home_comum(request):
    vagas = Vaga.objects.all()  # Recupera todas as vagas
    return render(request, 'home_comum.html', {'vagas': vagas})

def historico_comum(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')  # Recebe o CPF do formulário
        try:
            usuario = Cliente.objects.get(cpf=cpf)
            historico = HistoricoDeUso.objects.filter(usuario=usuario).order_by('id')  # Ordem crescente
            if not historico.exists():  # Verifica se o histórico está vazio
                messages.error(request, "Nenhum histórico encontrado para o CPF informado.")
            return render(request, 'historico_comum.html', {'historico': historico, 'cpf': cpf})
        except Cliente.DoesNotExist:
            messages.error(request, "CPF não encontrado.")
            return render(request, 'historico_comum.html', {'cpf': cpf})
    return render(request, 'historico_comum.html')
    
def registrar_entrada_comum(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        numero_vaga = request.POST.get('numero_vaga')

        # Verifica se o CPF está cadastrado no sistema
        if not Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF não cadastrado no sistema")
            return redirect('registrar_entrada_comum')

        # Valida se o número da vaga está no intervalo de 1 a 10
        if not numero_vaga.isdigit() or int(numero_vaga) < 1 or int(numero_vaga) > 10:
            messages.error(request, "Escolha uma vaga entre 1 e 10")
            return redirect('registrar_entrada_comum')

        # Verifica se a vaga está disponível
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Livre')
        except Vaga.DoesNotExist:
            messages.error(request, "Vaga não está livre!")
            return redirect('registrar_entrada_comum')

        # Atualiza os dados da vaga e registra o histórico
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Livre')
            vaga.cpf = cpf
            vaga.status = 'Ocupada'
            vaga.save()

            usuario = Cliente.objects.get(cpf=cpf)
            HistoricoDeUso.objects.create(usuario=usuario, vaga=vaga, acao='Entrada')  # Salva no histórico

            messages.success(request, f"Entrada registrada com sucesso na vaga {numero_vaga}!")
        except Exception as e:
            messages.error(request, f"Erro ao registrar entrada: {str(e)}")

        return redirect('registrar_entrada_comum')

    return render(request, 'registrar_entrada_comum.html')

def registrar_saida_comum(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        numero_vaga = request.POST.get('numero_vaga')

        # Verifica se o CPF está cadastrado no sistema
        if not Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF não cadastrado no sistema")
            return redirect('registrar_saida_comum')
        
        # Valida o número da vaga
        if not numero_vaga.isdigit() or int(numero_vaga) < 1 or int(numero_vaga) > 10:
            messages.error(request, "Número da vaga inválido. Escolha um número entre 1 e 10.")
            return redirect('registrar_saida_comum')

        # Verifica se a vaga está ocupada
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Ocupada')
            if vaga.cpf != cpf:
                messages.error(request, "O CPF informado não corresponde ao registro dessa vaga.")
                return redirect('registrar_saida_comum')
        except Vaga.DoesNotExist:
            messages.error(request, "Vaga não está ocupada!")
            return redirect('registrar_saida_comum')

        # Atualiza os dados da vaga e registra o histórico
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Ocupada')
            if vaga.cpf != cpf:
                messages.error(request, "O CPF informado não corresponde ao registro dessa vaga.")
                return redirect('registrar_saida_comum')

            usuario = Cliente.objects.get(cpf=cpf)
            HistoricoDeUso.objects.create(usuario=usuario, vaga=vaga, acao='Saída')  # Salva no histórico

            vaga.cpf = None
            vaga.status = 'Livre'
            vaga.save()

            messages.success(request, f"Saída registrada com sucesso para a vaga {numero_vaga}!")
        except Exception as e:
            messages.error(request, f"Erro ao registrar saída: {str(e)}")
            return redirect('registrar_saida_comum')

    return render(request, 'registrar_saida_comum.html')

def ver_planos(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')  # Obtém o CPF enviado no formulário
        # Verifica se o CPF está cadastrado no sistema
        if not Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF não cadastrado no sistema.")
            return redirect('ver_planos')

        try:     
            cliente = Cliente.objects.get(cpf=cpf)
            cliente.tipo = "VIP"  # Atualiza o status para VIP
            cliente.save()

            messages.success(request, "Agora você é um Cliente VIP! Faça Login novamente")
            return redirect('login')
        
        except Exception as e:
            messages.error(request, "Erro ao fazer upgrade")
            return redirect('ver_planos')
        
    return render(request, 'ver_planos.html')

def home_vip(request):
    vagas = Vaga.objects.all()  # Recupera todas as vagas
    return render(request, 'home_vip.html', {'vagas': vagas})

def historico_vip(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')  # Recebe o CPF do formulário
        try:
            usuario = Cliente.objects.get(cpf=cpf)
            historico = HistoricoDeUso.objects.filter(usuario=usuario).order_by('id')  # Ordem crescente
            if not historico.exists():  # Verifica se o histórico está vazio
                messages.error(request, "Nenhum histórico encontrado para o CPF informado.")
            return render(request, 'historico_vip.html', {'historico': historico, 'cpf': cpf})
        except Cliente.DoesNotExist:
            messages.error(request, "CPF não encontrado.")
            return render(request, 'historico_vip.html', {'cpf': cpf})
    return render(request, 'historico_vip.html')

def registrar_entrada_vip(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        numero_vaga = request.POST.get('numero_vaga')

        # Verifica se o CPF está cadastrado no sistema
        if not Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF não cadastrado no sistema")
            return redirect('registrar_entrada_vip')

        # Valida se o número da vaga está no intervalo de 1 a 10
        if not numero_vaga.isdigit() or int(numero_vaga) < 1 or int(numero_vaga) > 10:
            messages.error(request, "Escolha uma vaga entre 1 e 10")
            return redirect('registrar_entrada_vip')

        # Verifica se a vaga está disponível
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Livre')
        except Vaga.DoesNotExist:
            messages.error(request, "Vaga não está livre!")
            return redirect('registrar_entrada_vip')

        # Atualiza os dados da vaga e registra o histórico
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Livre')
            vaga.cpf = cpf
            vaga.status = 'Ocupada'
            vaga.save()

            usuario = Cliente.objects.get(cpf=cpf)
            HistoricoDeUso.objects.create(usuario=usuario, vaga=vaga, acao='Entrada')  # Salva no histórico

            messages.success(request, f"Entrada registrada com sucesso na vaga {numero_vaga}!")
        except Exception as e:
            messages.error(request, f"Erro ao registrar entrada: {str(e)}")

        return redirect('registrar_entrada_vip')

    return render(request, 'registrar_entrada_vip.html')

def registrar_saida_vip(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        numero_vaga = request.POST.get('numero_vaga')

        # Verifica se o CPF está cadastrado no sistema
        if not Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF não cadastrado no sistema")
            return redirect('registrar_saida_vip')
        # Valida o número da vaga
        if not numero_vaga.isdigit() or int(numero_vaga) < 1 or int(numero_vaga) > 10:
            messages.error(request, "Número da vaga inválido. Escolha um número entre 1 e 10.")
            return redirect('registrar_saida_vip')

        # Verifica se a vaga está ocupada
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Ocupada')
            if vaga.cpf != cpf:
                messages.error(request, "O CPF informado não corresponde ao registro dessa vaga.")
                return redirect('registrar_saida_vip')
        except Vaga.DoesNotExist:
            messages.error(request, "Vaga não está ocupada!")
            return redirect('registrar_saida_vip')

        # Atualiza os dados da vaga e registra o histórico
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Ocupada')
            if vaga.cpf != cpf:
                messages.error(request, "O CPF informado não corresponde ao registro dessa vaga.")
                return redirect('registrar_saida_vip')

            usuario = Cliente.objects.get(cpf=cpf)
            HistoricoDeUso.objects.create(usuario=usuario, vaga=vaga, acao='Saída')  # Salva no histórico

            vaga.cpf = None
            vaga.status = 'Livre'
            vaga.save()

            messages.success(request, f"Saída registrada com sucesso para a vaga {numero_vaga}!")
        except Exception as e:
            messages.error(request, f"Erro ao registrar saída: {str(e)}")
            return redirect('registrar_saida_vip')

    return render(request, 'registrar_saida_vip.html')

def meu_plano(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')  # Obtém o CPF enviado no formulário
        # Verifica se o CPF está cadastrado no sistema
        if not Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF não cadastrado no sistema.")
            return redirect('meu_plano')

        try:     
            cliente = Cliente.objects.get(cpf=cpf)
            if cliente.tipo =="VIP":
                cliente.tipo = "Comum"  # Atualiza o status para VIP
                cliente.save()

                messages.success(request, "Você voltou a ser Cliente Comum! Faça Login novamente")
                return redirect('login')
            else: 
                messages.error(request, "Este usuário não é VIP")
                return redirect('meu_plano')
        except Exception as e:
            messages.error(request, "Erro ao cancelar assinatura")
            return redirect('meu_plano')
        
    return render(request, 'meu_plano.html')

def reservar(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        numero_vaga = request.POST.get('numero_vaga')

        # Verifica se o CPF está cadastrado no sistema
        if not Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF não cadastrado no sistema")
            return redirect('reservar')

        # Valida se o número da vaga está no intervalo de 1 a 10
        if not numero_vaga.isdigit() or int(numero_vaga) < 1 or int(numero_vaga) > 10:
            messages.error(request, "Escolha uma vaga entre 1 e 10")
            return redirect('reservar')

        # Verifica se a vaga está disponível
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Livre')
        except Vaga.DoesNotExist:
            messages.error(request, "Vaga não está livre!")
            return redirect('reservar')

        # Atualiza os dados da vaga e registra o histórico
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Livre')
            vaga.cpf = cpf
            vaga.status = 'Reservada'
            vaga.save()

            usuario = Cliente.objects.get(cpf=cpf)
            HistoricoDeUso.objects.create(usuario=usuario, vaga=vaga, acao='Reserva')  # Salva no histórico

            messages.success(request, f"Vaga {numero_vaga} reservada com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao reservar vaga: {str(e)}")

        return redirect('reservar')

    return render(request, 'reservar.html')

def cancelar_reserva(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        numero_vaga = request.POST.get('numero_vaga')

        # Verifica se o CPF está cadastrado no sistema
        if not Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF não cadastrado no sistema")
            return redirect('cancelar_reserva')
        
        # Valida o número da vaga
        if not numero_vaga.isdigit() or int(numero_vaga) < 1 or int(numero_vaga) > 10:
            messages.error(request, "Número da vaga inválido. Escolha um número entre 1 e 10.")
            return redirect('cancelar_reserva')

        # Verifica se a vaga está reservada
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Reservada')
            if vaga.cpf != cpf:
                messages.error(request, "O CPF informado não corresponde ao registro dessa vaga.")
                return redirect('cancelar_reserva')
        except Vaga.DoesNotExist:
            messages.error(request, "Vaga não está reservada!")
            return redirect('cancelar_reserva')

        # Atualiza os dados da vaga e registra o histórico
        try:
            vaga = Vaga.objects.get(numero=numero_vaga, status='Reservada')
            if vaga.cpf != cpf:
                messages.error(request, "O CPF informado não corresponde ao registro dessa vaga.")
                return redirect('cancelar_reserva')

            usuario = Cliente.objects.get(cpf=cpf)
            HistoricoDeUso.objects.create(usuario=usuario, vaga=vaga, acao='Reserva')  # Salva no histórico

            vaga.cpf = None
            vaga.status = 'Livre'
            vaga.save()

            messages.success(request, f"Reserva da vaga {numero_vaga} cancelada!")
        except Exception as e:
            messages.error(request, f"Erro ao cancelar reserva: {str(e)}")
            return redirect('cancelar_reserva')

    return render(request, 'cancelar_reserva.html')