# Generated by Django 3.2.6 on 2021-10-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('direccion_proveedor', models.CharField(max_length=100)),
                ('telefono_proveedor', models.CharField(max_length=100)),
                ('ruc_proveedor', models.CharField(max_length=100)),
                ('email_proveedor', models.CharField(max_length=100)),
            ],
        ),
    ]
