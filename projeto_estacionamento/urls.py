from django.urls import path
import projeto_estacionamento.views as views

urlpatterns = [
    path('', views.login, name='login'),
    path('home_comum/', views.home_comum, name='home_comum'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('historico_comum/', views.historico_comum, name='historico_comum'),
    path('registrar_entrada_comum/', views.registrar_entrada_comum, name="registrar_entrada_comum"),
    path('registrar_saida_comum/', views.registrar_saida_comum, name="registrar_saida_comum"),
    path('ver_planos/', views.ver_planos, name='ver_planos'),
    path('login/', views.login, name='login'),
    path('home_vip', views.home_vip, name='home_vip'),
    path('historico_vip/', views.historico_vip, name='historico_vip'),
    path('registrar_entrada_vip/', views.registrar_entrada_vip, name="registrar_entrada_vip"),
    path('registrar_saida_vip/', views.registrar_saida_vip, name="registrar_saida_vip"),
    path('meu_plano/', views.meu_plano, name='meu_plano'),
    path('reservar/', views.reservar, name='reservar'),
    path('cancelar_reserva/', views.cancelar_reserva, name="cancelar_reserva"),
]