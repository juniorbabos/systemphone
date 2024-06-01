# Generated by Django 5.0.6 on 2024-05-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0011_alter_ordemservico_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservico',
            name='produto',
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='valor_lucro',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Valor Lucro'),
        ),
    ]