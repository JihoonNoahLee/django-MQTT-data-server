# Generated by Django 4.1.3 on 2022-11-15 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_server', '0002_alter_data_humidity_alter_data_temperature_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='time',
            new_name='date',
        ),
    ]
