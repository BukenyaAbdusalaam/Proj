# Generated by Django 4.1.7 on 2024-08-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0017_glass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfume_name', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('discount', models.CharField(max_length=10)),
                ('volume', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('date_of_extraction', models.DateField()),
            ],
        ),
    ]
