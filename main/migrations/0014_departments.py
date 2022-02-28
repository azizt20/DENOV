# Generated by Django 4.0 on 2022-02-03 11:48

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_departmentееее_centraldepartments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='pages/')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='pages/')),
                ('boss', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]