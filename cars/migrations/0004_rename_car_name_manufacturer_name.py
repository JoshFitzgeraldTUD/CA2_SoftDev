# Generated by Django 4.1.3 on 2022-11-22 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_remove_car_car_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturer',
            old_name='car_name',
            new_name='name',
        ),
    ]