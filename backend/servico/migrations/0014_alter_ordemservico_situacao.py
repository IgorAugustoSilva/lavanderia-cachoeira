# Generated by Django 4.2.3 on 2024-06-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0013_alter_ordemservicoitem_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='situacao',
            field=models.CharField(choices=[('la', 'Lavando'), ('pc', 'Pendente coleta'), ('pe', 'Pendente entrega'), ('en', 'Entregue')], max_length=2, verbose_name='Situação'),
        ),
    ]
