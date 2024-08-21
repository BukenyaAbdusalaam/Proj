from django.shortcuts import render

# Create your views here.
import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Product, Television, Tyres, Lubricants, Carpets, Car

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file, engine='openpyxl')

            # Iterate over the rows and create Product objects
            for index, row in df.iterrows():
                Product.objects.create(
                    wine_name=row['Wine Name'],
                    vintage=row['Vintage'],
                    price=row['Price'],
                    country_of_origin=row['Country Of Origin'],
                    grape_variety=row['Grape Variety'],
                    wine_type=row['Wine Type'],
                    
                    
                )
            return redirect('product_list')
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload.html', {'form': form})
# tele
def upload_television_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file, engine='openpyxl')
            for index, row in df.iterrows():
                Television.objects.create(
                    product=row['Product Name'],
                    currency=row['Currency'],
                    price=row['Prices'],
                    discount=row['Discounts'],
                    size=row['Size'],
                    description=row['Description']
                )
            return redirect('product_list')
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload_television.html', {'form': form})


def product_list(request, product_type=None):
    if product_type == 'wines':
        products = Product.objects.all()
    elif product_type == 'televisions':
        products = Television.objects.all()
    elif product_type == 'tyres':
        products = Tyres.objects.all()
    elif product_type == 'lubricants':
        products = Lubricants.objects.all()
    elif product_type == 'carpets':
        products = Carpets.objects.all()
    elif product_type == 'cars':
        products = Car.objects.all()
    else:
        products = None
    return render(request, 'myapp/product_list.html', {'products': products, 'product_type': product_type})




from datetime import datetime
from django.core.exceptions import ValidationError

from datetime import datetime, date

def validate_date(date_value):
    if isinstance(date_value, datetime):
        return date_value.date()  # Return the date part if it's already a datetime object
    elif isinstance(date_value, str):
        try:
            return datetime.strptime(date_value, '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError(f'Invalid date format: {date_value}')
    else:
        raise ValidationError(f'Expected string or datetime, got {type(date_value)}')


def upload_tyres_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        df = pd.read_excel(file)

        for _, row in df.iterrows():
            try:
                date_value = row['Date of extraction']
                date_value = validate_date(date_value) if pd.notna(date_value) else None

                Tyres.objects.create(
                    product_name=row['Product Name'],
                    brand_name=row['Brand Name'],
                    size=row['Size'],
                    load_speed=row['Load/Speed'],
                    price=row['Price(in USD$)'],
                    load_range=row['Load Range'],
                    performance_type=row['Performance Type'],
                    date_of_extraction=date_value,
                    source=row['Source']
                )
            except ValidationError as e:
                print(f"Validation error with row {row}: {e}")
                # Optionally, add code here to handle or log errors

        return render(request, 'upload_success.html')
    return render(request, 'myapp/upload_tyres.html')



# Querry search


from django.db.models import Q




from django.db.models import Q

def product_list(request, product_type):
    query = request.GET.get('q')
    
    if product_type == 'wines':
        products = Product.objects.all()
        if query:
            products = products.filter(
               Q(wine_name__icontains=query) |
                Q(country_of_origin__icontains=query) |
                Q(grape_variety__icontains=query) |
                Q(wine_type__icontains=query) |
                Q(vintage__icontains=query) 
            )
    elif product_type == 'televisions':
        products = Television.objects.all()
        if query:
            products = products.filter(
                Q(product__icontains=query) |
                Q(currency__icontains=query) |  
                Q(description__icontains=query) |
                Q(size__icontains=query) |
                Q(discount__icontains=query)
            )
    elif product_type == 'tyres':
        products = Tyres.objects.all()
        if query:
            products = products.filter(
                Q(product_name__icontains=query) |
                Q(brand_name__icontains=query) |
                Q(size__icontains=query) |
                Q(load_speed__icontains=query) |
                Q(load_range__icontains=query) |
                Q(performance_type__icontains=query) |
                Q(date_of_extraction__icontains=query) 
                
            )
    elif product_type == 'lubricants':
        products = Lubricants.objects.all()
        if query:
            products = products.filter(
                Q(product_name__icontains=query) |
                Q(capacity__icontains=query) |
                Q(measure__icontains=query) |
                Q(description__icontains=query) 
            )
    elif product_type == 'carpets':
        products = Carpets.objects.all()
        if query:
            products = products.filter(
                Q(product_name__icontains=query) |
                Q(size__icontains=query) |
                Q(measure__icontains=query) |
                Q(color__icontains=query) |
                Q(product_type__icontains=query) |
                Q(discount__icontains=query)
            )
    elif product_type == 'cars':
        products = Car.objects.all()
        if query:
            products = products.filter(
                Q(reference_number__icontains=query) |
                Q(mileage__icontains=query) |
                Q(year__icontains=query) |
                Q(engine__icontains=query) |
                Q(type__icontains=query) |
                Q(fuel_type__icontains=query)
            )
    else:
        products = None
    
    context = {
        'product_type': product_type,
        'products': products,
    }
    return render(request, 'myapp/product_list.html', context)



def upload_lubricant_file(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        
        # Load the uploaded Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file)

        # Iterate over the rows in the DataFrame and create Lubricants objects
        for index, row in df.iterrows():
            Lubricants.objects.create(
                product_name=row['Product Name'],
                price=row['Price'],
                currency=row['Currency'],
                capacity=row['Capacity'],
                measure=row['Measure'],
                description=row['Description'],
                date_of_extraction=row['Date of Extraction']
            )

        # Redirect or render a success page after processing
        return render(request, 'myapp/upload_success.html')

    return render(request, 'myapp/upload_lubricant.html')


def upload_carpets_file(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        df = pd.read_excel(excel_file)

        for _, row in df.iterrows():
            Carpets.objects.create(
                product_name=row['Product Name'],
                size=row['Size'],
                measure=row['Measure'],
                price=row['Price'],
                currency=row['Currency'],
                color=row['Color'],
                product_type=row['Product Type'],
                discount=row['Discount'],
                product_url=row['Product URL'],
                date_of_extraction=row['Date of Extraction']
            )

        return redirect('product_list', product_type='carpets')

    return render(request, 'myapp/upload_carpets.html')

from .models import Car

def upload_cars_file(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        df = pd.read_csv(csv_file)
        for _, row in df.iterrows():
            Car.objects.create(
                reference_number=row['Reference Number'],
                mileage=row['Mileage'],
                year=row['Year'],
                engine=row['Engine'],
                type=row['Type'],
                price=row['Price'],
                fuel_type=row['Fuel type'],
                date_of_extraction=row['Date of extraction'],
                source=row['Source']
            )
    return render(request, 'myapp/upload_cars.html')