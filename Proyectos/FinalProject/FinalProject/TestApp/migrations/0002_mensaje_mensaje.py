# Generated by Django 3.2.4 on 2021-07-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='mensaje',
            field=models.TextField(blank=True),
        ),
    ]
