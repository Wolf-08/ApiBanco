# Generated by Django 3.0.3 on 2020-02-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0007_auto_20200228_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentas',
            name='numero_tarjeta',
            field=models.CharField(max_length=15),
        ),
    ]