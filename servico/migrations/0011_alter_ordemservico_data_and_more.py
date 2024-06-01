# Generated by Django 5.0.6 on 2024-05-24 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0010_remove_ordemservico_quantidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data do Serviço'),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='valor_custo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Valor Custo'),
        ),
    ]