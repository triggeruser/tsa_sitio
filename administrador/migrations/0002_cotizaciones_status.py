# Generated by Django 3.2.4 on 2021-06-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizaciones',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]