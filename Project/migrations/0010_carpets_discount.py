# Generated by Django 4.1.7 on 2024-08-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0009_carpets'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpets',
            name='discount',
            field=models.CharField(default='No Discount', max_length=50),
        ),
    ]
