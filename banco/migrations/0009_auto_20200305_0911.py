# Generated by Django 3.0.3 on 2020-03-05 15:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0008_auto_20200228_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentas',
            name='fecha_consulta',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='CuentaCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_consultaC', models.DateTimeField(default=django.utils.timezone.now)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.Clientes')),
                ('cuenta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.Cuentas')),
            ],
        ),
    ]
