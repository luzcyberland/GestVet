# Generated by Django 3.2.6 on 2021-10-20 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pacientes', '0002_alter_paciente_id_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id_vacuna', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_vacunacion', models.DateField()),
                ('vacuna_usada', models.CharField(max_length=50)),
                ('tipo_vacuna', models.CharField(max_length=50)),
                ('fecha_revacunacion', models.DateField()),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.paciente')),
            ],
        ),
    ]