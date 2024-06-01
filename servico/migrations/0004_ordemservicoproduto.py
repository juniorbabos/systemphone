# Generated by Django 5.0.6 on 2024-05-21 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_cliente'),
        ('servico', '0003_remove_servico_cliente_remove_servico_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServicoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto_servico', to='estoque.product', verbose_name='produto serviço')),
            ],
        ),
    ]