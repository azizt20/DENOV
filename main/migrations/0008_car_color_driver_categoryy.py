# Generated by Django 4.0 on 2022-02-02 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_department_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('second_name', models.CharField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=17, null=True)),
                ('phone_number_second', models.CharField(max_length=17, null=True)),
                ('car_number', models.CharField(max_length=20, null=True)),
                ('car_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.color')),
                ('car_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.car')),
            ],
        ),
        migrations.CreateModel(
            name='Categoryy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('drivers', models.ManyToManyField(to='main.Driver')),
            ],
        ),
    ]
