# Generated by Django 3.2.4 on 2021-07-05 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0009_delete_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.moneda'),
        ),
    ]
