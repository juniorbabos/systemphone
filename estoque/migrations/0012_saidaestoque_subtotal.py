# Generated by Django 5.0.6 on 2024-05-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0011_saidaestoque_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidaestoque',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=1, editable=False, max_digits=10),
            preserve_default=False,
        ),
    ]