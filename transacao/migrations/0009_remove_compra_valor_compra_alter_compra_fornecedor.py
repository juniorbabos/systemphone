# Generated by Django 5.0.6 on 2024-05-23 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0008_alter_compra_fornecedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='valor_compra',
        ),
        migrations.AlterField(
            model_name='compra',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transacao.fornecedor'),
        ),
    ]