# Generated by Django 5.0.6 on 2024-05-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0007_alter_saidaestoque_saldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidaestoque',
            name='data',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
