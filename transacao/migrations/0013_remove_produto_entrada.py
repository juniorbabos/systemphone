# Generated by Django 5.0.6 on 2024-05-24 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0012_alter_produto_entrada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='entrada',
        ),
    ]