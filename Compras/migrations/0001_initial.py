# Generated by Django 3.2.6 on 2021-10-26 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventario', '0008_alter_productoservicio_existencia'),
        ('Proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaCompra',
            fields=[
                ('id_factura_compra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_factura', models.DateTimeField()),
                ('subTotal', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('monto_exento', models.FloatField(default=0)),
                ('monto_iva', models.FloatField(default=0)),
                ('monto_gravado', models.FloatField(default=0)),
                ('estado_factura_compra', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')], default='Pendiente', max_length=20)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proveedores.proveedor')),
            ],
            options={
                'verbose_name': 'FacturaCompra',
                'verbose_name_plural': 'FacturasCompras',
            },
        ),
        migrations.CreateModel(
            name='DetalleFacturaCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(default=0.0)),
                ('precio', models.FloatField(default=0)),
                ('subTotalDetalle', models.FloatField(default=0)),
                ('descuentoDetalle', models.FloatField(default=0)),
                ('totalDetalle', models.FloatField(default=0)),
                ('monto_exento_det', models.FloatField(default=0)),
                ('monto_iva_det', models.FloatField(default=0)),
                ('monto_gravado_det', models.FloatField(default=0)),
                ('factura_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Compras.facturacompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.productoservicio')),
            ],
            options={
                'verbose_name': 'Detalle factura',
                'verbose_name_plural': 'Detalle facturas',
            },
        ),
    ]
