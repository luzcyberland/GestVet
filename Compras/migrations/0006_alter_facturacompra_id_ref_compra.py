# Generated by Django 3.2.6 on 2021-11-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0005_facturacompra_id_ref_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacompra',
            name='id_ref_compra',
            field=models.IntegerField(default=0),
        ),
    ]