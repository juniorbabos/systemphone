# Generated by Django 5.0.6 on 2024-05-23 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_remove_cliente_endereco2'),
        ('transacao', '0007_delete_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
        ),
    ]
