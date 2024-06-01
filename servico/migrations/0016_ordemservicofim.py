# Generated by Django 5.0.6 on 2024-05-31 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0015_alter_ordemservico_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServicoFim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_custo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Valor Custo')),
                ('valor_lucro', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Valor Lucro')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Valor total')),
                ('conclusao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('os', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servico.ordemservico')),
            ],
        ),
    ]
