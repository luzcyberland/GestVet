# Generated by Django 3.2.6 on 2021-11-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0005_auto_20211030_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
