from django.contrib import admin

from .models import Product, Television, Tyres, Lubricants, Carpets

admin.site.register(Product)
admin.site.register(Television)
admin.site.register(Tyres)
admin.site.register(Lubricants)
admin.site.register(Carpets)