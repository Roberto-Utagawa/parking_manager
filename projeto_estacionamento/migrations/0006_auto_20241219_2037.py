# Generated by Django 3.2.25 on 2024-12-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_estacionamento', '0005_auto_20241219_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11),
        ),
    ]
