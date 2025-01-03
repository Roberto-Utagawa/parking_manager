# Generated by Django 3.2.25 on 2024-12-19 23:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_estacionamento', '0003_cliente_tipo_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('status', models.CharField(choices=[('Livre', 'Livre'), ('Ocupada', 'Ocupada'), ('Reservada', 'Reservada')], default='Livre', max_length=10)),
            ],
        ),
    ]
