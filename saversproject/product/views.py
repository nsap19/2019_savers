from django.shortcuts import render
from .models import *

# Create your views here.
def product(request):
    products = Product.objects
    properties = ProductProperty.objects
    return render(request, 'product/product.html', {'products':products, 'properties':properties})

    
def detail(request, pk):
    product = Product.objects.get(pk=pk)
    properties = ProductProperty.objects.filter(product_id=pk)
    propertynames = PropertyName.objects
    grouped = dict()
    for obj in properties.all():
        # grouped.setdefault(obj.property, []).append([obj.property_value, obj.product.id])
        pname = obj.property.property_name
        grouped.setdefault(pname, []).append(obj.property_value)

    return render(request, 'product/detail.html',{'product':product, 'properties':properties, 'grouped': grouped})
