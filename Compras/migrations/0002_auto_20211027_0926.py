# Generated by Django 3.2.6 on 2021-10-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturacompra',
            name='estado_factura_compra',
        ),
        migrations.AddField(
            model_name='facturacompra',
            name='numero_factura',
            field=models.CharField(default=1, max_length=50),
        ),
    ]