# Generated by Django 3.1.5 on 2021-02-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='issued_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='component',
            name='type',
            field=models.IntegerField(choices=[(0, 'Batteries and Chargers'), (1, 'Development Boards'), (2, 'Drivers'), (3, 'Electronic Tools'), (4, 'Mechanical Tools'), (5, 'Robotics KIT'), (6, 'Sensors'), (7, 'Others')], default=7),
        ),
    ]