# Generated by Django 4.2.3 on 2024-08-24 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0032_ordemservico_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservico',
            name='servico',
        ),
    ]