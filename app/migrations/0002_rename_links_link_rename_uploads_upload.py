# Generated by Django 4.0.4 on 2022-11-19 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
        migrations.RenameModel(
            old_name='Uploads',
            new_name='Upload',
        ),
    ]