# Generated by Django 4.2.3 on 2024-08-12 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0023_alter_ordemservico_data_coleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='preco_only_view',
            field=models.CharField(default='10', max_length=10, verbose_name='Preço'),
        ),
    ]