# Generated by Django 3.0.3 on 2020-02-24 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0002_auto_20200224_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='cuenta',
            old_name='cuenta_id',
            new_name='id',
        ),
    ]
