# Generated by Django 4.1.7 on 2024-08-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0013_alter_car_mileage_alter_car_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='engine_type',
            new_name='engine',
        ),
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.CharField(default='Not Mentioned', max_length=100),
        ),
    ]