# Generated by Django 4.1.3 on 2022-11-22 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stream',
            new_name='Manufacturer',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='stream',
            new_name='Manufacturer',
        ),
    ]