# Generated by Django 3.2.4 on 2021-07-02 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20210614_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='capaciodad',
            new_name='capacidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Cotizaciones',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]
