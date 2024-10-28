# Generated by Django 4.2.3 on 2024-06-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0010_alter_ordemservicoitem_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservicoitem',
            name='tipo',
            field=models.CharField(choices=[('sl', 'Só lavar'), ('lp', 'Lavar e passar'), ('sp', 'Só passar'), ('na', 'Não se aplica')], default='na', max_length=2, verbose_name='Tipo'),
            preserve_default=False,
        ),
    ]
