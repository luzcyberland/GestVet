# Generated by Django 3.2.6 on 2021-10-10 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0006_alter_productoservicio_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoservicio',
            name='porc_iva',
            field=models.IntegerField(default=0),
        ),
    ]