# Generated by Django 5.0.6 on 2024-05-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0006_saidaestoque_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saidaestoque',
            name='saldo',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
