# Generated by Django 4.2.3 on 2024-08-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0024_servico_preco_only_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='preco_only_view',
        ),
        migrations.AddField(
            model_name='servico',
            name='preco_only_view_lavar',
            field=models.CharField(default='99999', max_length=6, verbose_name='Preço'),
        ),
        migrations.AddField(
            model_name='servico',
            name='preco_only_view_lavarpassar',
            field=models.CharField(default='99999', max_length=6, verbose_name='Preço'),
        ),
        migrations.AddField(
            model_name='servico',
            name='preco_only_view_passar',
            field=models.CharField(default='99999', max_length=6, verbose_name='Preço'),
        ),
    ]
