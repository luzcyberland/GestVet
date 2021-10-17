# Generated by Django 3.2.6 on 2021-10-03 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(help_text='Descripción de la marca', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id_unidad_medida', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoServicio',
            fields=[
                ('id_producto_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('codigoBarra', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.FloatField(default=0)),
                ('existencia', models.IntegerField(default=0)),
                ('ultimaCompra', models.DateField(blank=True, null=True)),
                ('es_producto', models.BooleanField(default=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
                ('unidadMedida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.unidadmedida')),
            ],
        ),
    ]