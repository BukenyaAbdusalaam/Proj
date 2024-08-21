# Generated by Django 4.1.7 on 2024-08-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0011_alter_carpets_product_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('engine_type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fuel_type', models.CharField(max_length=50)),
                ('date_of_extraction', models.DateField()),
                ('source', models.CharField(max_length=255)),
            ],
        ),
    ]