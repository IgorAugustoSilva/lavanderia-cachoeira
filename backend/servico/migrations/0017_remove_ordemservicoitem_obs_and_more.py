# Generated by Django 4.2.3 on 2024-06-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0016_ordemservicoitem_obs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservicoitem',
            name='obs',
        ),
        migrations.AddField(
            model_name='ordemservicoitem',
            name='observacao',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Observação'),
        ),
    ]
