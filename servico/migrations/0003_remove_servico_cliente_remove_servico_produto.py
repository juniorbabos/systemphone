# Generated by Django 5.0.6 on 2024-05-21 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0002_ordemservico_ordemservicoitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='produto',
        ),
    ]
