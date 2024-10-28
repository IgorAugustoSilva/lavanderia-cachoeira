# Generated by Django 4.2.3 on 2024-06-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0014_alter_ordemservico_situacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservicoitem',
            name='proxima_visita',
        ),
        migrations.AddField(
            model_name='ordemservicoitem',
            name='previsao_entrega',
            field=models.DateField(blank=True, null=True, verbose_name='Previsão de entrega'),
        ),
    ]
