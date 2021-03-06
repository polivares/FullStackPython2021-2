# Generated by Django 3.2.9 on 2021-11-23 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('run', models.IntegerField()),
                ('dv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_cuenta', models.IntegerField()),
                ('saldo', models.FloatField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.cliente')),
            ],
        ),
    ]
