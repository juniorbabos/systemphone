# Generated by Django 5.0.6 on 2024-05-19 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='estoque_max',
        ),
    ]
