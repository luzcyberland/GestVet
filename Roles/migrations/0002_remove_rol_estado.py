# Generated by Django 3.1.6 on 2021-09-05 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Roles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='estado',
        ),
    ]