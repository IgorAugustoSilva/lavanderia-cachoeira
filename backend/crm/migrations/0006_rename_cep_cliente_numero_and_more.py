# Generated by Django 4.2.3 on 2024-06-18 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_cliente_razao_social'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cep',
            new_name='numero',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='endereco',
            new_name='rua',
        ),
    ]
