# Generated by Django 3.2.4 on 2021-07-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0012_auto_20210712_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='telefono_cliente',
            field=models.CharField(max_length=10),
        ),
    ]
