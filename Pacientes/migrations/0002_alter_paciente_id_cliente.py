# Generated by Django 3.2.2 on 2021-09-07 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_alter_cliente_cedula_cliente'),
        ('Pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='id_cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Clientes.cliente'),
        ),
    ]