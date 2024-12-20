from django.db import models
from django.utils.timezone import now
import uuid  # Para gerar IDs únicos

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # ID único
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)  # Garantir que o CPF é único
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=128)  # Armazenar senhas hash (seguros)

    # Tipo de usuário
    TIPO_USUARIO_CHOICES = [
        ('Comum', 'Comum'),
        ('VIP', 'VIP'),
    ]
    tipo = models.CharField(
        max_length=5,
        choices=TIPO_USUARIO_CHOICES,
        default='Comum'  # Valor padrão
    )

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
    
class Vaga(models.Model):
    # ID único para cada vaga
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.PositiveIntegerField(unique=True)  # Número da vaga (ex: 1, 2, 3)

    # Status da vaga
    STATUS_CHOICES = [
        ('Livre', 'Livre'),
        ('Ocupada', 'Ocupada'),
        ('Reservada', 'Reservada'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Livre'  # Status padrão
    )

    cpf = models.CharField(max_length=14, blank=True, null=True)  # CPF do cliente

    def __str__(self):
        return f"Vaga {self.numero} ({self.status})"
    
class HistoricoDeUso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey('Cliente', on_delete=models.CASCADE)  # Relacionado ao usuário
    vaga = models.ForeignKey('Vaga', on_delete=models.CASCADE)  # Relacionado à vaga
    acao = models.CharField(max_length=10, choices=[('Entrada', 'Entrada'), ('Saída', 'Saída'), ('Reserva', 'Reserva')])  # Tipo de ação

    def __str__(self):
        return f"{self.usuario.nome} - {self.acao} na vaga {self.vaga.numero}"