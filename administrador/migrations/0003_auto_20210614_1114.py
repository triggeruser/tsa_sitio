# Generated by Django 3.2.4 on 2021-06-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_cotizaciones_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='municipio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estado',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
