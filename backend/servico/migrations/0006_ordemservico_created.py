# Generated by Django 4.2.3 on 2024-06-17 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0005_remove_ordemservico_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='criado em'),
            preserve_default=False,
        ),
    ]
