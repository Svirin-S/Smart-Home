# Generated by Django 4.1.4 on 2022-12-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
