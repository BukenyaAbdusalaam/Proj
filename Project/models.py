from django.db import models
from datetime import date
# Create your models here.

from django.db import models

class Product(models.Model):
    wine_name = models.CharField(max_length=100)
    vintage = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    grape_variety = models.CharField(max_length=100)
    wine_type = models.CharField(max_length=100)
    
   

# televisions

class Television(models.Model):
    product = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    discount = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    description  = models.CharField(max_length=50)
    # date_of_extraction = models.DateField(default=date(2024, 8, 10))
    # source = models.CharField(max_length=255, default='https://www.dubaistore.com/ae-en/search?all-categories-home=&q=television')


  

class Tyres(models.Model):
    product_name = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    load_speed = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    load_range = models.CharField(max_length=50)
    performance_type = models.CharField(max_length=50)
    date_of_extraction = models.DateField()
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name
    

class Lubricants(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    capacity = models.CharField(max_length=50)
    measure = models.CharField(max_length=50)
    description = models.TextField()
    date_of_extraction = models.DateField()



class Carpets(models.Model):
    product_name = models.CharField(max_length=255)
    size = models.CharField(max_length=100)
    measure = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    product_type = models.CharField(max_length=100)
    discount = models.CharField(max_length=50, default='No Discount')
    product_url = models.CharField(max_length=100)
    date_of_extraction = models.DateField()

    


class Car(models.Model):
    reference_number = models.CharField(max_length=100)
    mileage = models.IntegerField()
    year = models.CharField(max_length=50)
    engine = models.CharField(max_length=100)  # Engine
    type = models.CharField(max_length=100)    # Type
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=50)
    date_of_extraction = models.DateField()
    source = models.CharField(max_length=255)

  
class Glass(models.Model):
    product_name = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    price =  models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    min_order =  models.CharField(max_length=100)
    measure = models.CharField(max_length=100)
    date_of_extraction = models.DateField(auto_now_add=True)

from django.db import models

class Perfume(models.Model):
    perfume_name = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    discount = models.CharField(max_length=10)
    volume = models.CharField(max_length=100)
    url = models.URLField()
    date_of_extraction = models.DateField()

  