from django.urls import path
import projeto_estacionamento.views as views

urlpatterns = [
    path('', views.login, name='login'),
    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('homeFuncionario/', views.homeFuncionario, name='homeFuncionario'),
    path('homeCliente/', views.homeCliente, name='homeCliente'),
    path('reservar_funcionario/', views.reservar_funcionario,name='reservar_funcionario'),
    path('cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('cancelar_funcionario/', views.cancelar_funcionario, name='cancelar_funcionario'),
    path('reservar_cliente/', views.reservar_cliente, name='reservar_cliente'),
    path('cancelar_cliente/', views.cancelar_cliente, name='cancelar_cliente'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('vagasdisponiveis_cliente', views.vagasdisponiveis_cliente, name="vagasdisponiveis_cliente"),
    path('removercliente', views.removercliente, name="removercliente"),
    path('vagasdisponiveis_funcionario', views.vagasdisponiveis_funcionario, name='vagasdisponiveis_funcionario'),
    path('remover_vaga', views.remover_vaga, name='remover_vaga'),
    path('cadastrar_funcionario', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('remover_funcionario', views.remover_funcionario, name='remover_funcionario'),
]