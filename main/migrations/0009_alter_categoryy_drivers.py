# Generated by Django 4.0 on 2022-02-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_car_color_driver_categoryy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryy',
            name='drivers',
            field=models.ManyToManyField(to='main.Car'),
        ),
    ]