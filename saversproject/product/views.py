from django.shortcuts import get_object_or_404, render, redirect
from .models import *

# Create your views here.
def product(request):
    products = Product.objects
    properties = ProductProperty.objects
    propertynames = PropertyName.objects
    grouped = dict() 
    for obj in properties.all():
        pname = obj.property.property_name
        pid = obj.product_id
        grouped.setdefault(pname, []).append([obj.property_value, pid])

    # for obj in properties.all():
    #     pid = obj.product_id
    #     pname = obj.property.property_name
    #     grouped.setdefault(pname, []).append(pid)
    # for key, value in grouped.items():
    #     pname = obj.property.property_name
    #     p = obj.property_value
    #     grouped2.setdefault(pname, []).append(p)
    #     for k,val in grouped2.items():
    #         if key == k:
    #             grouped[key].append(val)
                

    # scorecard = {}
    # for st, score in zip(pname, p):
    #     scorecard[st] = dict(zip(pid,p))

    # for obj in properties.all():
    #     pname = obj.property.property_name
    #     p = obj.property_value
    #     grouped2.setdefault(grouped,[]).append(p)
    # current_user_pk = request.user.id
    

    return render(request, 'product/product.html', {'products':products, 'properties':properties, 'grouped': grouped })

    
def detail(request, pk):
    product = Product.objects.get(pk=pk)
    properties = ProductProperty.objects.filter(product_id=pk)
    propertynames = PropertyName.objects
    grouped = dict() 
    for obj in properties.all():
        # grouped.setdefault(obj.property, []).append([obj.property_value, obj.product.id])
        pname = obj.property.property_name
        grouped.setdefault(pname, []).append(obj.property_value)
    # current_user_pk = request.user.id
    return render(request, 'product/detail.html',{'product':product, 'properties':properties, 'grouped': grouped})

