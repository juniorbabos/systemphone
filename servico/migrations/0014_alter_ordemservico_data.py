# Generated by Django 5.0.6 on 2024-05-31 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0013_remove_ordemservico_valor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='data',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Serviço'),
        ),
    ]
