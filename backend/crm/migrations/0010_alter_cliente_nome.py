# Generated by Django 4.2.3 on 2024-06-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_cliente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=120, unique=True, verbose_name='nome'),
        ),
    ]
