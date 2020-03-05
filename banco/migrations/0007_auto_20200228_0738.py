# Generated by Django 3.0.3 on 2020-02-28 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0006_auto_20200228_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentas',
            name='numero_tarjeta',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxLengthValidator(16), django.core.validators.MinLengthValidator(15)]),
        ),
    ]
