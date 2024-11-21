from django.urls import path
from .views import upload_file, upload_television_file, product_list, upload_glass_file
from . import views

urlpatterns = [
    path('', product_list, {'product_type': 'wines'}, name='home'),
    path('upload/', upload_file, name='upload_file'),
    path('television/', upload_television_file, name='upload_television_file'),
    path('upload_tyres/', views.upload_tyres_file, name='upload_tyres'),
    path('tyres/', views.product_list, {'category': 'tyres'}, name='product_list_tyres'),
    path('products_list/<str:product_type>/', product_list, name='product_list'),
    path('upload_lubricant/', views.upload_lubricant_file, name='upload_lubricant'),
    path('upload_carpets/', views.upload_carpets_file, name='upload_carpets'),
    path('upload_cars/', views.upload_cars_file, name='upload_cars'),
    path('upload_glass/', upload_glass_file, name='upload_glass'),
    path('upload_perfumes/', views.upload_perfumes_file, name='upload_perfumes'),

]
